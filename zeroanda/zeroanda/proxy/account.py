from zeroanda.models import AccountModel, AccountInfoModel
from zeroanda.proxy.streaming import Streaming
from zeroanda import utils
from zeroanda.constant import INSTRUMENTS, ACCOUNT_STATUS
from zeroanda.cache import etag

from django.conf import settings

import math

class AccountProxyModel:
    _accountModel = None
    _accountInfoModel = None
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def _add_account(self, response):
        accountModel = AccountModel(
            account_id = response.get_body()['accounts'][0]['accountId'],
            account_currency = response.get_body()['accounts'][0]['accountCurrency'],
            account_name = response.get_body()['accounts'][0]['accountName'],
            margin_rate = response.get_body()['accounts'][0]['marginRate'],
            etag = response.get_etag(),
            status = ACCOUNT_STATUS[0][0],
        )
        accountModel.save()
        return accountModel

    def _add_account_info(self, accountModel, response):
        accountInfoModel = AccountInfoModel(
            account_model   = accountModel,
            account_id      = response.get_body()['accountId'],
            account_currency= response.get_body()['accountCurrency'],
            account_name    = response.get_body()['accountName'],
            balance         = response.get_body()['balance'],
            margin_rate     = response.get_body()['marginRate'],
            margin_used     = response.get_body()['marginUsed'],
            margin_avail    = response.get_body()['marginAvail'],
            open_orders     = response.get_body()['openOrders'],
            open_trades     = response.get_body()['openTrades'],
            unrealized_pl   = response.get_body()['unrealizedPl'],
            realized_pl     = response.get_body()['realizedPl'],
            etag            = response.get_etag(),
        )
        accountInfoModel.save()
        return accountInfoModel

    def _disable_all(self):
        AccountModel.objects.filter(status=ACCOUNT_STATUS[0][0]).update(status=ACCOUNT_STATUS[1][0])

    def _get_account_model(self):
        accounts = AccountModel.objects.filter(status=ACCOUNT_STATUS[0][0]).order_by('created')
        if len(accounts) > 1:
            self._disable_all()

        self._accountModel = None if len(accounts) == 0 else accounts.reverse()[0]
        account_response = self._streaming.accounts(None if self._accountModel == None else self._accountModel.etag )

        if self._accountModel == None:
            self._accountModel = self._add_account(account_response)
        elif account_response.get_code() != 304:
            self._disable_all()
            self._accountModel = self._add_account(account_response)

    def _get_account_info_model(self):
        account_info_list = AccountInfoModel.objects.filter(account_model = self._accountModel).order_by('created')
        self._accountInfoModel = None if len(account_info_list) == 0 else account_info_list.reverse()[0]
        account_info_response = self._streaming.account_info(self._accountModel)

        if self._accountInfoModel == None:
            self._accountInfoModel = self._add_account_info(self._accountModel, account_info_response)
        elif account_info_response.get_code() != 304:
            self._accountInfoModel = self._add_account_info(self._accountModel, account_info_response)

    def get_account(self):
        if self._accountModel == None:
            self._get_account_model()
            self._get_account_info_model()

        return self._accountModel

    def get_account_info(self):
        self.get_account()
        if self._accountInfoModel == None:
            self._get_account_info_model()

        return self._accountInfoModel

    def update_account(self):
        self._get_account_model()
        self._get_account_info_model()

        return self._accountModel

    def update_account_info(self):
        if self._accountModel == None:
            self._get_account_model()
        self._get_account_info_model()

        return self._accountInfoModel

    def get_max_units(self, rate):
        self.get_account_info()
        if self._accountInfoModel == None:
            return 0
        units = self._accountInfoModel.balance * settings.LEVERAGE / rate / settings.CURRENCY;
        # utils.info("balance: " + str(self._accountInfoModel.balance) + ", leverage: " + str(settings.LEVERAGE) + ", rate: " + str(rate) + ", currency: " + str(settings.CURRENCY) + ", units: " + str(units))
        return int(math.floor(units))