import  logging
import math
import time
from datetime import datetime, timedelta

from zeroanda import utils
from zeroanda.proxy.streaming import Streaming
from zeroanda.errors import ZeroandaError
from zeroanda.models import PricesModel, AccountModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.order import OrderProxyModel

logger =logging.getLogger("django")

class OrderProcess:
    _scheduleModel   = None
    _accountModel    = None
    _latest_ask = None
    _latest_bid = None
    _targetdate = None
    _streaming  = None
    _order      = None

    def __init__(self, schedule):
        super(OrderProcess,self).__init__()
        self._scheduleModel = schedule
        self._targetdate = datetime.now() + timedelta(minutes=1)
        self._streaming = Streaming()
        self._order = OrderProxyModel()

        self.get_account()

    @staticmethod
    def create(schedule):
        return OrderProcess(schedule)

    def get_account(self):
        self._accountModel = AccountProxyModel().get_account()

    def run(self):
        # return
        i = 0
        while True:
            try:
                remain_time = self._targetdate.timestamp() - datetime.now().timestamp()
                print(remain_time)
                if remain_time > self._scheduleModel.priority:
                    self.collect_prices()
                # else:
                self.demo_buy()
                # self.get_orders()
                i += 1

                nexttime = math.floor((datetime.now() + timedelta(seconds=1)).timestamp())
                duration = nexttime - datetime.now().timestamp()

                time.sleep(duration)

                if i >= 1:
                    break
            except:
                print("exception.")
                break

    def collect_prices(self):
        model = PricesModel(schedule=self._scheduleModel, begin=datetime.now())
        model.save()
        try :
            result = self._streaming.prices(self._scheduleModel.country)
            logger.info(result)
            model.ask   = self._latest_ask = result["ask"]
            model.bid   = self._latest_bid = result["bid"]
            model.instrument    = result["instrument"]
            model.time = datetime.fromtimestamp(utils.format_unixtime(result["time"]))
            model.end = datetime.now()
            elapsed = model.end - model.begin
            model.elapsed = str(elapsed)
            model.save()
        except ZeroandaError as e:
            print(e)
            e.save()
        except Exception as e:
            print(e)

    def get_orders(self):
        try:
            result = self._streaming.get_orders(self._account)
        except ZeroandaError as e:
            print('error')
            e.save()
        except Exception as e:
            print(e)

    def order(self):
        buy_target_price = self._latest_ask + 0.2
        sell_target_price = self._latest_ask - 0.2
        # try :
        #     self.buy_ifdoco(buy_target_price)
        #     self.sell_ifdoco(sell_target_price)
        # except ZeroandaError as e:
        #     print('error')
        #     e.save()

    # def buy_ifdoco(self, target_price, instrument, units):
    #     try :
    #         # [logger.info(item) for item in INSTRUMENTS if item[0] == instrument]
    #         # return
    #         model = OrderModel(schedule=self._schedule,
    #                            # instruments = [instrument for item in INSTRUMENTS if item[0] == instrument],
    #                            instruments = instrument,
    #                            units = units,
    #                            side = SIDE[0][0],
    #                            type = TYPE[2][1],
    #                            # expirey= '',
    #                            price=target_price,
    #                            upperBound=target_price + 10.0,
    #                            lowerBound=target_price - 10.0,
    #                            status=ACTUAL_ORDER_STATUS[0][0]
    #                            )
    #
    #         model.save()
    #         result = self._streaming.order_ifdoco(self._account, model)
    #     except ZeroandaError as e:
    #         print('error')
    #         e.save()

    # def sell_ifdoco(self, target_price, instrument):
    #
    #     try :
    #         result = self._streaming.order_ifdoco(self._account, instrument, 'buy', target_price, target_price - 0.5, target_price + 0.5)
    #     except ZeroandaError as e:
    #         print('error')
    #         e.save()

    def test_order_buy(self):
        self.collect_prices()
        self._order.buy_ifdoco(self._accountModel, self._scheduleModel, self._latest_ask + 10, 2)

    # def test_get_orders(self):
    #     self._streaming.get_orders(self._accountModel)
