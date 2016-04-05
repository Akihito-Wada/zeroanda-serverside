import logging
import math
import time
from datetime import datetime, timedelta
from multiprocessing import Process

from zeroanda import utils
from zeroanda.classes.utils import timeutils
from zeroanda.proxy.streaming import Streaming
from zeroanda.errors import ZeroandaError
from zeroanda.models import PricesModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.prices import PricesProxyModel

logger =logging.getLogger("django")

class OrderProcess:
    _scheduleModel   = None
    _accountModelProxy    = None
    _latest_ask = None
    _latest_bid = None
    _targetdate = None
    _streaming  = None
    _order      = None

    # def __init__(self, schedule):
    def __init__(self):
        super(OrderProcess,self).__init__()
        # self._scheduleModel = schedule
        self._targetdate = datetime.now() + timedelta(minutes=1)
        # self._streaming = Streaming()
        # self._order = OrderProxyModel()
        self.get_account()

    @staticmethod
    def create(schedule):
        orderProcess = OrderProcess()
        orderProcess._scheduleModel = schedule
        orderProcess._streaming = Streaming()
        orderProcess._order = OrderProxyModel()
        return orderProcess

    def get_account(self):
        self._accountModelProxy = AccountProxyModel()

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
            model.ask   = self._latest_ask = result["ask"]
            model.bid   = self._latest_bid = result["bid"]
            model.instrument    = result["instrument"]
            model.time = timeutils.convert_timestamp2datetime(result["time"])
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
            result = self._streaming.get_orders(self._account.account_id)
        except ZeroandaError as e:
            print('error')
            e.save()
        except Exception as e:
            print(e)

    def collect_prices2(self):
        # proxyModel = PricesProxyModel(self._scheduleModel)
        # proxyModel.get_price()
        count = 5
        duration = 1 / count
        logger.info(duration)
        jobs = []
        for x in range(10):
            job = Process(target=self.f)
            jobs.append(job)
            job.start()
            time.sleep(duration)
        [job.join() for job in jobs]

    def f(self):
        proxyModel = PricesProxyModel(self._scheduleModel)
        proxyModel.get_price()

    def test_order_buy(self, ask):
        proxyModel = PricesProxyModel(self._scheduleModel)
        price = proxyModel.get_price()

        units = self._accountModelProxy.get_max_units(price.ask)
        # self._order.buy_ifdoco(self._accountModelProxy.get_account(), self._scheduleModel, ask + 0.01, units)

    def test_order_sell(self, bid):
        # self.collect_prices()
        units = self._accountModelProxy.get_max_units(bid)
        self._order.sell_ifdoco(self._accountModelProxy.get_account(), self._scheduleModel, bid - 10, units)

    def test_ifdoco(self, instrument):
        proxyModel = PricesProxyModel()
        price = proxyModel.get_price(instrument)
        units = int(math.floor(self._accountModelProxy.get_max_units(price.bid) / 2))

        jobs = []
        job = Process(target=self._order.sell_ifdoco, args=(self._accountModelProxy.get_account(), self._scheduleModel, price.bid - 100, units))
        jobs.append(job)
        job.start()
        job = Process(target=self._order.buy_ifdoco, args=(self._accountModelProxy.get_account(), self._scheduleModel, price.ask + 100, units))
        jobs.append(job)
        job.start()

        [job.join() for job in jobs]

    def test_ticking_price(self):
        i = 0
        while True:
            try:
                remain_time = self._targetdate.timestamp() - datetime.now().timestamp()
                utils.info(remain_time)
                # if remain_time > self._scheduleModel.priority:
                self.collect_prices2()
                # else:
                i += 1

                nexttime = math.floor((datetime.now() + timedelta(seconds=1)).timestamp())
                duration = nexttime - datetime.now().timestamp()

                time.sleep(duration)

                if i >= 1:
                    break
            except:
                print("exception.")
                break
        return

    def countdown(self, targetdate, exec):
        i = 0
        while True:
            try:
                remain_time = targetdate.timestamp() - datetime.now().timestamp()
                utils.info(targetdate)
                utils.info(remain_time)

                exec()

                nexttime = math.floor((datetime.now() + timedelta(seconds=1)).timestamp())
                duration = nexttime - datetime.now().timestamp()

                time.sleep(duration)

                if remain_time < 0:
                    break

            except:
                print("exception.")
                break
        return
