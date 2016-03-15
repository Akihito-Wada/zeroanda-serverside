from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.utils import timeutils
from zeroanda.proxy.order import OrderProxyModel

class GetOrderProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        self.__orderProxyModel = OrderProxyModel()
        super(GetOrderProcess, self).__init__(task)

    def _create_job(self):pass

    def _get_orders(self):
        orderProxyModel = OrderProxyModel()
        orderProxyModel.get_orders(accountModel)