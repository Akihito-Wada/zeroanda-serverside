import multiprocessing
from datetime import datetime, timedelta
import time
import math
import random
from multiprocessing import Process
from zeroanda.models import ProcessModel, PricesModel, AccountModel, ErrorModel
from zeroanda import utils
from zeroanda import streaming
from zeroanda.streaming import Streaming
from zeroanda.errors import ZeroandaError
from zeroanda.constant import PRIORITY
import types
import types
class OrderProcess:
    _schedule   = None
    _account    = None
    _latest_ask = None
    _latest_bid = None
    _targetdate = None
    _streaming  = None

    def __init__(self, schedule):
        super(OrderProcess,self).__init__()
        self._schedule = schedule
        self._targetdate = datetime.now() + timedelta(minutes=1)
        self._streaming = Streaming()

        result = self._streaming.accounts()
        result = self._streaming.accounts(result['accounts'][0]['accountId'])
        self._account = AccountModel(
                            schedule    = schedule,
                            account_id = result['accountId'],
                            margin_rate = result['marginRate'],
                            account_currency = result['accountCurrency'],
                            account_name = result['accountName'],
                            balance    = result['balance'],
                            open_orders= result['openOrders'],
                            open_trades= result['openTrades'],
                            unrealized_pl= result['unrealizedPl'],
                            realized_pl= result['realizedPl'],
                            margin_avail= result['marginAvail'],
                            margin_used= result['marginUsed'],
        )
        # self._account['balance']    = result['balance']
        # self._account['open_orders']= result['openOrders']
        # self._account['open_trades']= result['openTrades']
        # self._account['unrealized_pl']= result['unrealizedPl']
        # self._account['realized_pl']= result['realizedPl']
        # self._account['margin_avail']= result['marginAvail']
        # self._account['margin_used']= result['marginUsed']

        print(result)
        self._account.save()

    @staticmethod
    def create(schedule):
        return OrderProcess(schedule)

    def run(self):
        # return
        i = 0
        while True:
            try:
                remain_time = self._targetdate.timestamp() - datetime.now().timestamp()
                print(remain_time)
                if remain_time > self._schedule.priority:
                    self.collect_prices()
                # else:
                #     self.order()

                i += 1

                nexttime = math.floor((datetime.now() + timedelta(seconds=1)).timestamp())
                duration = nexttime - datetime.now().timestamp()

                time.sleep(duration)

                if i >= 3:
                    break
            except:
                print("exception.")
                break

    def collect_prices(self):
        model = PricesModel(schedule=self._schedule, begin=datetime.now())
        model.save()
        try :
            result = self._streaming.prices(self._schedule.country)

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
        self._streaming.get_orders()

    def order(self, account):
        buy_target_price = self._latest_ask + 0.2
        sell_target_price = self._latest_ask - 0.2
        try :
            self._streaming.order_ifdoco('buy', buy_target_price, buy_target_price + 0.5, buy_target_price - 0.5)
            self._streaming.order_ifdoco('sell', sell_target_price, sell_target_price - 0.5, sell_target_price + 0.5)
        except ZeroandaError as e:
            print('error')
            e.save()
