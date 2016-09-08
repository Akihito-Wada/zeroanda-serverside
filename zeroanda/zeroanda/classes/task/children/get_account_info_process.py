from django import db
from django.conf import settings

from datetime import timedelta
from multiprocessing import Process

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.utils import timeutils
from zeroanda.classes.utils.loggerutils import Logger
from zeroanda.models import TradeTransactionModel
from zeroanda.proxy.setting import SettingProxy
from zeroanda.proxy.account import AccountProxyModel
from zeroanda import utils


class GetAccountInfoProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(GetAccountInfoProcess, self).__init__(task)

        self._set_target_date()

    def _create_job(self):
        self._jobs.append(Process(target=self._get_latest_account_info()))

    def _get_latest_account_info(self):
        accountProxyModel = AccountProxyModel()
        accountProxyModel.get_latest_account_info()

    def _is_condition(self):
        now = timeutils.get_now_with_jst()
        Logger.info(self.__class__.__name__ + "::_is_condition::now: " + str(now) + ", target_date: " + str(self._target_date))
        # if now > self._target_date:
        #     raise Exception('target time has already passed.')
        result = now > self._target_date
        if result == True:
            db.close_old_connections()
            self.__transaction_model.excute_time = timeutils.get_now_with_jst()
            self.__transaction_model.save()
        return result

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        # self._target_date = self._presentation_date + timedelta(seconds = settings.DURATION_GET_ACCOUNT_INFO_EXCUTE_TIME)
        self._target_date = self._presentation_date + timedelta(seconds=SettingProxy.get_account_info_excute_time(self._get_priority()))
        self.__transaction_model = TradeTransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date, transaction_name=self.__class__.__name__)
        self.__transaction_model.save()
