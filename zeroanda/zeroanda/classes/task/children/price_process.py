from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda import utils

from multiprocessing import Process

class PriceProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(PriceProcess, self).__init__(task)

    def _create_job(self):
        self._jobs.append(Process(target=self._get_price))

    def _get_price(self):
        priceProxyModel = PricesProxyModel()
        self._task.set_price_model(priceProxyModel.get_price("USD_JPY"))

    def _is_condition(self):
        return True