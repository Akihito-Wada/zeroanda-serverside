import logging
from datetime import timedelta

from django.conf import settings

from zeroanda   import utils
from zeroanda.classes.net.streaming import Streaming
from zeroanda.classes.utils import timeutils
from zeroanda.constant import SIDE, TYPE, ACTUAL_ORDER_STATUS, ERROR_CODE, ORDER_STATUS
from zeroanda.errors import ZeroandaError
from zeroanda.models import OrderModel, ActualOrderModel

logger =logging.getLogger("django")

class OrderProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def _add_actual_order(self, response, orderModel, scheduleModel = None):
        result = response.get_body()
        actualOrderModel = ActualOrderModel(
            trade_id=orderModel.trade_id,
            schedule= scheduleModel,
            order = orderModel,
            actual_order_id=result["orderOpened"]["id"],
            instruments = result["instrument"],
            units = result["orderOpened"]["units"],
            side = result["orderOpened"]["side"],
            expiry = timeutils.convert_timestamp2datetime(result["orderOpened"]["expiry"]),
            price = result["price"],
            upperBound = result["orderOpened"]["upperBound"],
            lowerBound = result["orderOpened"]["lowerBound"],
            stopLoss = result["orderOpened"]["stopLoss"],
            takeProfit = result["orderOpened"]["takeProfit"],
            trailingStop = result["orderOpened"]["trailingStop"],
            time = timeutils.convert_timestamp2datetime(result["time"]),
        )
        actualOrderModel.save()
        return actualOrderModel

    '''
    ticket
    '''
    def get_orders(self, account_id=None, trade_id=None, side=None):
        if account_id != None:
            result = self._streaming.get_orders(account_id)
            return result.get_body()

    def get_order_by_trade_id(self, trade_id, side):
        models = OrderModel.objects.filter(trade_id=trade_id, side=side)
        if len(models) > 0:
            utils.info(models[0].actual_model.actual_order_id)
            return models[0]
        else:
            return None

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
                account_id=accountModel.account_id,
                instruments=instruments,
                units=units,
                side=SIDE[1][0],
                expiry=expiry,
                upperBound=upperBound,
                lowerBound=lowerBound
            )
            if response.get_code() == 201:
                self._add_actual_order(response, orderModel, scheduleModel)
        except ZeroandaError as e:
            e.save()
            orderModel.status = ORDER_STATUS[1][0]
            orderModel.updated  = timeutils.get_now_with_jst()
            orderModel.save()
            return

    def buy_ifdoco(self, target_price, upper_bound, lower_bound, take_profit, stop_loss, units, expiry = None, accountModel = None, scheduleModel = None, accountId = None, instrument = None, trade_id=0):
        try :
            _instrument = instrument if instrument != None else scheduleModel.country
            _expiry = expiry if expiry != None else scheduleModel.presentation_time + timedelta(seconds=settings.EXPIRY_SECONDS)
            orderModel = OrderModel(
                            trade_id=trade_id,
                            schedule=scheduleModel,
                            instruments = _instrument,
                            units = units,
                            side = SIDE[1][0],
                            type = TYPE[2][0],
                            expiry = _expiry,
                            price=target_price,
                            upperBound=upper_bound,
                            lowerBound=lower_bound,
                            takeProfit=take_profit,
                            stopLoss=stop_loss,
                            status=ORDER_STATUS[0][0]
                            )
            orderModel.save()
            response = self._streaming.order_ifdoco(
                account_id=accountId if accountId != None else accountModel.account_id,
                instruments=_instrument,
                units=units,
                side=SIDE[1][0],
                expiry=_expiry,
                price=target_price,
                upperBound=upper_bound,
                lowerBound=lower_bound,
                takeProfit=take_profit,
                stopLoss=stop_loss
            )
            if response.get_code() == 201:
                return self._add_actual_order(response, orderModel, scheduleModel)
        except ZeroandaError as e:
            e.save()
            orderModel.status = ORDER_STATUS[1][0]
            orderModel.updated  = timeutils.get_now_with_jst()
            orderModel.save()
            return

    def sell_ifdoco(self, target_price, upper_bound, lower_bound, take_profit, stop_loss, units, expiry = None, accountModel = None, scheduleModel = None, accountId = None, instrument = None, trade_id=0):
        _instrument = instrument if instrument != None else scheduleModel.country
        _expiry = expiry if expiry != None else scheduleModel.presentation_time + timedelta(seconds=settings.EXPIRY_SECONDS)
        try :
            orderModel = OrderModel(
                            trade_id=trade_id,
                            schedule=scheduleModel,
                            instruments = _instrument,
                            units = units,
                            side = SIDE[0][0],
                            type = TYPE[2][0],
                            expiry = _expiry,
                            price=target_price,
                            upperBound=upper_bound,
                            lowerBound=lower_bound,
                            takeProfit=take_profit,
                            stopLoss=stop_loss,
                            status=ORDER_STATUS[0][0]
                            )
            orderModel.save()

            response = self._streaming.order_ifdoco(
                account_id=accountId if accountId != None else accountModel.account_id,
                instruments=_instrument,
                units=units,
                side=SIDE[0][0],
                expiry=_expiry,
                price=target_price,
                upperBound=upper_bound,
                lowerBound=lower_bound,
                takeProfit=take_profit,
                stopLoss=stop_loss
            )
            # response = self._streaming.order_ifdoco(accountModel, orderModel)
            if response.get_code() == 201:
                return self._add_actual_order(response, orderModel, scheduleModel)
        except ZeroandaError as e:
            e.save()
            orderModel.status = ORDER_STATUS[1][0]
            orderModel.updated  = timeutils.get_now_with_jst()
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
            actualOrderModel = self.get_actual_order_model(trade_id)
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
            actualOrderModel = self.get_actual_order_model(actual_order_id)
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
        result = self.get_orders(accountModel.account_id)
        for v in result['orders']:
            self.cancel(accountModel, v["id"])

    def _update_order(self, order_id):
        orderModel = OrderModel.objects.get(pk=order_id)
        orderModel.updated  = timeutils.get_now_with_jst()
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
    def get_actual_order_model(self, actual_order_id):
        try:
            return ActualOrderModel.objects.get(actual_order_id=actual_order_id)
        except ActualOrderModel.DoesNotExist as e:
            return None

    '''
    ActualOrderModelのエラーコードを更新
    args: {actual_order_id, error_code}
    '''
    def _update_error_code(self, actual_order_id, error_code):
        actualOrderModel = self.get_actual_order_model(actual_order_id)
        actualOrderModel.status = ACTUAL_ORDER_STATUS[1][0]
        actualOrderModel.error_code = error_code
        actualOrderModel.updated    = timeutils.get_now_with_jst()
        actualOrderModel.save()

    def _cancel_actual_order(self, actual_order_id):
        actualOrderModel = self.get_actual_order_model(actual_order_id)
        actualOrderModel.status = ACTUAL_ORDER_STATUS[2][0]
        actualOrderModel.updated    = timeutils.get_now_with_jst()
        actualOrderModel.save()
    #

