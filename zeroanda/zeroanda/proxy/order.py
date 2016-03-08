from zeroanda.models import OrderModel, ActualOrderModel
from zeroanda.constant import SIDE, TYPE, ACTUAL_ORDER_STATUS, INSTRUMENTS, ERROR_CODE, ORDER_STATUS
from zeroanda.errors import ZeroandaError
from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

from datetime import timedelta, datetime
import math
import logging
logger =logging.getLogger("django")

class OrderProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def _add_actual_order(self, response, scheduleModel, orderModel):
        utils.info(response.get_body())
        result = response.get_body()
        # price = response.get_body()['prices'][0]
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
        return actualOrderModel

    '''
    ticket
    '''
    def get_orders(self, accountModel):
        result = self._streaming.get_orders(accountModel)
        utils.info(result.get_body())
        return result.get_body()

    def buy_market(self, accountModel, instruments, units, scheduleModel=None, expiry=None, upperBound=None, lowerBound=None):
        try :
            orderModel = OrderModel(
                            schedule=scheduleModel,
                            instruments = instruments,
                            units = units,
                            side = SIDE[1][0],
                            type = TYPE[2][0],
                            expiry = expiry,
                            upperBound=upperBound,
                            lowerBound=lowerBound,
                            status=ORDER_STATUS[0][0]
                            )
            orderModel.save()
            response = self._streaming.order_market(
                accountModel.account_id,
                instruments,
                units,
                SIDE[1][0],
                expiry,
                upperBound,
                lowerBound
            )
            if response.get_code() == 201:
                self._add_actual_order(response, scheduleModel, orderModel)
        except ZeroandaError as e:
            e.save()
            orderModel.status = ORDER_STATUS[1][0]
            orderModel.updated  = datetime.now()
            orderModel.save()
            return

    def buy_ifdoco(self, accountModel, scheduleModel, target_price, units):
        try :
            orderModel = OrderModel(
                            schedule=scheduleModel,
                            instruments = scheduleModel.country,
                            units = units,
                            side = SIDE[1][0],
                            type = TYPE[2][0],
                            expiry = scheduleModel.presentation_time + timedelta(minutes=1),
                            price=target_price,
                            upperBound=self._get_ask_upper_bound(target_price),
                            lowerBound=self._get_ask_lower_bound(target_price),
                            status=ORDER_STATUS[0][0]
                            )
            orderModel.save()
            utils.info('test')
            response = self._streaming.order_ifdoco(
                accountModel.account_id,
                scheduleModel.country,
                units,
                SIDE[1][0],
                scheduleModel.presentation_time + timedelta(minutes=1),
                target_price,
                self._get_ask_upper_bound(target_price),
                self._get_ask_lower_bound(target_price)
            )
            utils.info('test1')
            # response = self._streaming.order_ifdoco(accountModel, orderModel)
            if response.get_code() == 201:
                self._add_actual_order(response, scheduleModel, orderModel)
        except ZeroandaError as e:
            e.save()
            orderModel.status = ORDER_STATUS[1][0]
            orderModel.updated  = datetime.now()
            orderModel.save()
            return

    def sell_ifdoco(self, accountModel, scheduleModel, target_price, units):
        try :
            orderModel = OrderModel(
                            schedule=scheduleModel,
                            instruments = scheduleModel.country,
                            units = units,
                            side = SIDE[0][0],
                            type = TYPE[2][0],
                            expiry = scheduleModel.presentation_time + timedelta(minutes=1),
                            price=target_price,
                            upperBound=self._get_bid_upper_bound(target_price),
                            lowerBound=self._get_bid_lower_bound(target_price),
                            status=ORDER_STATUS[0][0]
                            )
            orderModel.save()

            response = self._streaming.order_ifdoco(
                accountModel.account_id,
                scheduleModel.country,
                units,
                SIDE[0][0],
                scheduleModel.presentation_time + timedelta(minutes=1),
                target_price,
                self._get_bid_upper_bound(target_price),
                self._get_bid_lower_bound(target_price)
            )
            # response = self._streaming.order_ifdoco(accountModel, orderModel)
            if response.get_code() == 201:
                self._add_actual_order(response, scheduleModel, orderModel)
        except ZeroandaError as e:
            e.save()
            orderModel.status = ORDER_STATUS[1][0]
            orderModel.updated  = datetime.now()
            orderModel.save()
            return

    # def traders(self, accountModel):
    #     self._streaming.traders(accountModel, INSTRUMENTS[0][0])
    #     # self._streaming.traders(accountModel, scheduleModel.instruments, INSTRUMENTS[0][0])

    # def positions(self, accountModel):
    #     result = self._streaming.positions(accountModel)
    #     utils.info(result.get_body())

    def delete(self, accountModel, trade_id):
        try:
            self._streaming.cancel_order(accountModel, trade_id)
            self._cancel_actual_order(trade_id);
            actualOrderModel = self._get_actual_order_model(trade_id)
            self._update_order(actualOrderModel.order.id)
        except ZeroandaError as e:
            actualOrderModel = self._get_active_actual_order_model(trade_id)
            if ERROR_CODE[1][0] == e.get_code():
                self._update_error_code(trade_id, e.get_code())
            self._update_order(actualOrderModel.order.id)
            e.save()
        except Exception as e:
            utils.error(e)
        finally:
            return

    def cancel(self, accountModel, actual_order_id):
        try:
            self._streaming.cancel_order(accountModel, actual_order_id)
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
            utils.error(e)
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

    def _get_ask_upper_bound(self, reference_value):
        # return ('%.3f', reference_value + 10.0)
        return math.floor((reference_value + 0.1) * 1000) / 1000
        # return reference_value + 10.0

    def _get_ask_lower_bound(self, reference_value):
        # return ('%.3f', reference_value - 10.0)
        return math.floor((reference_value - 0.1) * 1000) / 1000
        # return reference_value - 10.0

    def _get_bid_upper_bound(self, reference_value):
        # return ('%.3f', reference_value + 10.0)
        return math.floor((reference_value + 0.1) * 1000) / 1000
        # return reference_value + 10.0

    def _get_bid_lower_bound(self, reference_value):
        # return ('%.3f', reference_value - 10.0)
        return math.floor((reference_value - 0.1) * 1000) / 1000
        # return reference_value - 10.0

