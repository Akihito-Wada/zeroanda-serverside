from django.conf import settings

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.utils import timeutils
from zeroanda.proxy.order import OrderProxyModel

from multiprocessing import Process

class GetOrderProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        self.__orderProxyModel = OrderProxyModel()
        super(GetOrderProcess, self).__init__(task)

    def _create_job(self):
        self._jobs.append(Process(target=self._get_orders))

    def _get_orders(self):
        orderProxyModel = OrderProxyModel()
        self._task.set_orders_model(orderProxyModel.get_orders(self._task.pool['account_info_model'].account_id))

    def _is_condition(self):
        if settings.TEST == True:
            return True
        return True