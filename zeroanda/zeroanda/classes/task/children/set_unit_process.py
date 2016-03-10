from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda import utils

from multiprocessing import Process

class SetUnitProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(SetUnitProcess, self).__init__(task)

    def _create_job(self):
        self._jobs.append(Process(target=self._set_unit))

    def _set_unit(self):
        utils.info(self._task)
        utils.info(self._task.pool)

        # utils.info('set_unit')
        # utils.info(self._task._account_info_model)
        # utils.info(utils.get_max_units(self._task._account_info_model.balance, self._price_model.ask))
        # utils.info(utils.get_max_units(self._task._account_info_model.balance, self._price_model.bid))

    def _is_condition(self):
        return True