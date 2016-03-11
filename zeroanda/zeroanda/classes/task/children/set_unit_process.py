from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda import utils

from multiprocessing import Process

class SetUnitProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(SetUnitProcess, self).__init__(task)

    def _create_job(self):
        self._jobs.append(Process(target=self._set_unit))

    def _set_unit(self):
        # utils.info(self._task.pool)
        # utils.info(self._task.pool['account_info_model'])
        # utils.info(self._task.pool['account_info_model'].balance)
        # utils.info(self._task.pool['price_model'])
        # utils.info(self._task.pool['price_model'].ask)
        # utils.info(self._task.pool['price_model'].bid)
        # utils.info(utils.get_max_units(int(self._task.pool['account_info_model'].balance), self._task.pool['price_model'].ask))
        # utils.info(utils.get_max_units(int(self._task.pool['account_info_model'].balance), self._task.pool['price_model'].bid))

        self._task.pool['ask_unit'] = utils.get_max_units(int(self._task.pool['account_info_model'].balance), self._task.pool['price_model'].ask)
        self._task.pool['bid_unit'] = utils.get_max_units(int(self._task.pool['account_info_model'].balance), self._task.pool['price_model'].bid)

    def _is_condition(self):
        return True