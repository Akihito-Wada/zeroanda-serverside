from django.conf import settings

from datetime import datetime, timedelta
from multiprocessing import Process

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.constant import DURATION_GET_ACCOUNT_EXCUTE_TIME
from zeroanda.models import TransactionModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda import utils

class GetAccountProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(GetAccountProcess, self).__init__(task)

        self._set_target_date()

    def _create_job(self):
        self._jobs.append(Process(target=self._get_account))

    def _get_account(self):
        accountProxyModel = AccountProxyModel()
        accountProxyModel.get_account_info()
        self._task.set_account_info_model(accountProxyModel.get_account_info())

    def _is_condition(self):
        now = datetime.now()
        utils.info('test1')
        utils.info(now)
        utils.info(self._target_date)
        utils.info(self._presentation_date)
        utils.info('test2')
        if now > self._presentation_date:
            raise Exception('presentation time has already passed.')
        result = now > self._target_date
        if result == True:
            self.__transaction_model.excute_time = datetime.now()
            self.__transaction_model.save()
        return result

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        self._target_date = self._presentation_date + timedelta(seconds = DURATION_GET_ACCOUNT_EXCUTE_TIME)

        self.__transaction_model = TransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date, transaction_name=self.__class__.__name__)
        self.__transaction_model.save()
