from django.conf import settings
from datetime import datetime, timedelta

from zeroanda.classes.task.children.aprocess import AbstractProcess
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
        now = datetime.now()
        utils.info(now)
        utils.info(self._presentation_date)
        if now > self._presentation_date:
            raise Exception('presentation time has already passed.')
        return True

    def _set_target_date(self):
        # self._presentation_date = datetime.now() + timedelta(seconds = SET_UNIT_EXCUTE_TIME) * 2 if settings.TEST else self._task.schedule.presentation_time
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
