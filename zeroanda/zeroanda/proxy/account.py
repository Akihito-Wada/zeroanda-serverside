from zeroanda.models import AccountModel
from zeroanda.proxy.streaming import Streaming
from zeroanda import utils

from django.conf import settings

import math

class AccountProxyModel:
    accountModel = None
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_account(self):
        result = self._streaming.accounts()
        result = self._streaming.accounts(result['accounts'][0]['accountId'])
        self.accountModel = AccountModel(
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
        self.accountModel.save()
        return self.accountModel

    def get_max_units(self, rate):
        self.get_account()
        if self.accountModel == None:
            return 0
        units = self.accountModel.balance * settings.LEVERAGE / rate / settings.CURRENCY;
        utils.info("balance: " + str(self.accountModel.balance) + ", leverage: " + str(settings.LEVERAGE) + ", rate: " + str(rate) + ", currency: " + str(settings.CURRENCY) + ", units: " + str(units))
        return math.floor(units)