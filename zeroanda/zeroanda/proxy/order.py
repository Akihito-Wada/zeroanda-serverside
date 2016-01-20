from zeroanda.models import OrderModel, ActualOrderModel
from zeroanda.constant import SIDE, TYPE, ACTUAL_ORDER_STATUS, INSTRUMENTS, ERROR_CODE, ORDER_STATUS
from zeroanda.errors import ZeroandaError
from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

from datetime import timedelta, datetime
import logging
logger =logging.getLogger("django")

class OrderProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_orders(self, accountModel):
        result = self._streaming.get_orders(accountModel)
        return result

    def buy_ifdoco(self, accountModel, scheduleModel, target_price, units):
        try :
            orderModel = OrderModel(
                            schedule=scheduleModel,
                            instruments = scheduleModel.country,
                            units = str(units),
                            side = SIDE[1][0],
                            type = TYPE[2][0],
                            expiry = scheduleModel.presentation_time + timedelta(minutes=1),
                            price=target_price,
                            upperBound=self._get_upper_bound(target_price),
                            lowerBound=self._get_lower_bound(target_price),
                            status=ORDER_STATUS[0][0]
                            )
            orderModel.save()
            result = self._streaming.order_ifdoco(accountModel, orderModel)

            actualOrderModel = ActualOrderModel(
                schedule= scheduleModel,
                order = orderModel,
                actual_order_id=result["orderOpened"]["id"],
                instruments = result["instrument"],
                units = result["orderOpened"]["units"],
                side = result["orderOpened"]["side"],
                expiry = utils.convert_timestamp2datetime(result["orderOpened"]["expiry"]),
                price = result["price"],
                upperBound = result["orderOpened"]["upperBound"],
                lowerBound = result["orderOpened"]["lowerBound"],
                stopLoss = result["orderOpened"]["stopLoss"],
                takeProfit = result["orderOpened"]["takeProfit"],
                trailingStop = result["orderOpened"]["trailingStop"],
                time = utils.convert_timestamp2datetime(result["time"]),
            )
            actualOrderModel.save()
        except ZeroandaError as e:
            e.save()
            orderModel.status = ORDER_STATUS[1][0]
            orderModel.updated  = datetime.now()
            orderModel.save()
            return

    def sell_ifdoco(self, accountModel, target_price, instrument):
        try :
            result = self._streaming.order_ifdoco(accountModel, instrument, 'buy', target_price, target_price - 0.5, target_price + 0.5)
        except ZeroandaError as e:
            utils.output(e)
            e.save()

    def traders(self, accountModel):
        self._streaming.traders(accountModel, INSTRUMENTS[0][0])
        # self._streaming.traders(accountModel, scheduleModel.instruments, INSTRUMENTS[0][0])

    def cancel(self, accountModel, actual_order_id):
        try:
            result = self._streaming.cancel_order(accountModel, actual_order_id)
            logger.info(result)

            self._cancel_actual_order(actual_order_id);
            actualOrderModel = self._get_actual_order_model(actual_order_id)
            self._update_order(actualOrderModel.order.id)
        except ZeroandaError as e:
            actualOrderModel = self._get_active_actual_order_model(actual_order_id)
            if ERROR_CODE[1][0] == e.get_code():
                self._update_error_code(actual_order_id, e.get_code())
            self._update_order(actualOrderModel.order.id)
            e.save()
        except Exception as e:
            utils.output(e)
        finally:
            return

    def cancel_all(self, accountModel):
        result = self.get_orders(accountModel)
        for v in result['orders']:
            self.cancel(accountModel, v["id"])

    def _update_order(self, order_id):
        orderModel = OrderModel.objects.get(pk=order_id)
        orderModel.updated  = datetime.now()
        orderModel.save()

    '''
    アクティブなActualOrderModelを取得
    args: {actual_order_id}
    '''
    def _get_active_actual_order_model(self, actual_order_id):
        try :
            return ActualOrderModel.objects.get(actual_order_id=actual_order_id, status=ACTUAL_ORDER_STATUS[0][0])
        except ActualOrderModel.DoesNotExist as e:
            raise Exception(e)


    '''
    ActualOrderModelを取得
    args: {actual_order_id}
    '''
    def _get_actual_order_model(self, actual_order_id):
        try:
            return ActualOrderModel.objects.get(actual_order_id=actual_order_id)
        except ActualOrderModel.DoesNotExist as e:
            raise Exception(e)

    '''
    ActualOrderModelのエラーコードを更新
    args: {actual_order_id, error_code}
    '''
    def _update_error_code(self, actual_order_id, error_code):
        actualOrderModel = self._get_actual_order_model(actual_order_id)
        actualOrderModel.status = ACTUAL_ORDER_STATUS[1][0]
        actualOrderModel.error_code = error_code
        actualOrderModel.updated    = datetime.now()
        actualOrderModel.save()

    def _cancel_actual_order(self, actual_order_id):
        actualOrderModel = self._get_actual_order_model(actual_order_id)
        actualOrderModel.status = ACTUAL_ORDER_STATUS[2][0]
        actualOrderModel.updated    = datetime.now()
        actualOrderModel.save()

    def _get_upper_bound(self, reference_value):
        return reference_value + 10.0,

    def _get_lower_bound(self, reference_value):
        return reference_value - 10.0,
