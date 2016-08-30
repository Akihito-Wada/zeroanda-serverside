from django import db
from django.conf import settings

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.utils import timeutils
from zeroanda.classes.utils.loggerutils import Logger
from zeroanda.models import TradeTransactionModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.trades import TradesProxyModel

from zeroanda import utils

from datetime import timedelta

from multiprocessing import Process

class CloseTradesProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        self.__orderProxyModel = OrderProxyModel()
        super(CloseTradesProcess, self).__init__(task)

        self._set_target_date()

    def _create_job(self):
        self._jobs.append(Process(target=self._close_trades))

    def _close_trades(self):
        db.close_old_connections()

        accountModel = AccountProxyModel().get_account()
        tradesProxyModel = TradesProxyModel();
        tradesProxyModel.close_all_trades(accountModel)

    def _is_condition(self):
        now = timeutils.get_now_with_jst()
        Logger.info(self.__class__.__name__ + "::_is_condition::now: " + str(now) + ", target_date: " + str(self._target_date))
        result = now > self._target_date
        if result == True:
            db.close_old_connections()
            self.__transaction_model.excute_time = timeutils.get_now_with_jst()
            self.__transaction_model.save()
        return result

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        self._target_date = self._presentation_date + timedelta(seconds = settings.CLOSE_ALL_TRADES_EXCUTE_TIME)
        self.__transaction_model = TradeTransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date, transaction_name=self.__class__.__name__)
        self.__transaction_model.save()
