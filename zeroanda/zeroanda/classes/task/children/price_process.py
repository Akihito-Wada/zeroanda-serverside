from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda import utils

class PriceProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(PriceProcess, self).__init__(task)

    def _exec(self):
        utils.info(333)
        priceProxyModel = PricesProxyModel()
        self._task.set_price_model(priceProxyModel.get_price("USD_JPY"))