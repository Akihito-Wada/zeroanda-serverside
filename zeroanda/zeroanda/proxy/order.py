from zeroanda.models import OrderModel
from zeroanda.constant import SIDE, TYPE, ACTUAL_ORDER_STATUS
from zeroanda.errors import ZeroandaError
from zeroanda.proxy.streaming import Streaming
from zeroanda.constant import INSTRUMENTS

from datetime import timedelta
import logging
logger =logging.getLogger("django")

class OrderProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get(self, accountModel):
        self._streaming.get_orders(accountModel)

    def buy_ifdoco(self, accountModel, scheduleModel, target_price, units):
        orderModel = OrderModel(
                        schedule=scheduleModel,
                        instruments = scheduleModel.country,
                        units = units,
                        side = SIDE[1][0],
                        type = TYPE[2][0],
                        expirey = scheduleModel.presentation_time + timedelta(minutes=1),
                        price=target_price,
                        upperBound=target_price + 10.0,
                        lowerBound=target_price - 10.0,
                        status=ACTUAL_ORDER_STATUS[0][0]
                        )
        orderModel.save()
        result = self._streaming.order_ifdoco(accountModel, orderModel)

    def sell_ifdoco(self, accountModel, target_price, instrument):
        try :
            result = self._streaming.order_ifdoco(accountModel, instrument, 'buy', target_price, target_price - 0.5, target_price + 0.5)
        except ZeroandaError as e:
            print('error')
            e.save()

    def traders(self, accountModel):
        self._streaming.traders(accountModel, INSTRUMENTS[0][0])