from django.conf import settings

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.utils import timeutils
from zeroanda.models import TradeTransactionModel
from zeroanda import utils

from multiprocessing import Process

class SetUnitProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(SetUnitProcess, self).__init__(task)

        self._set_target_date()

    def _create_job(self):
        self._jobs.append(Process(target=self._set_unit))

    def _set_unit(self):
        self._task.pool['ask_unit'] = utils.get_max_units(int(self._task.pool['account_info_model'].balance), self._task.pool['price_model'].ask)
        self._task.pool['bid_unit'] = utils.get_max_units(int(self._task.pool['account_info_model'].balance), self._task.pool['price_model'].bid)

    def _is_condition(self):
        now = timeutils.get_now_with_jst()
        if now > self._presentation_date:
            raise Exception('presentation time has already passed.')

        self.__transaction_model.excute_time = now
        self.__transaction_model.save()
        return True

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time

        self.__transaction_model = TradeTransactionModel(trade_model=self._task.trade_model, transaction_name=self.__class__.__name__)
        self.__transaction_model.save()