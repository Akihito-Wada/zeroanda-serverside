from django.conf import settings
from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda import utils
from zeroanda.constant import DURATION_GET_PRICE

from multiprocessing import Process
from zeroanda.classes.utils import timeutils

class GetPriceProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(GetPriceProcess, self).__init__(task)

    def _create_job(self):
        self._jobs.append(Process(target=self._get_price))

    def _get_price(self):
        priceProxyModel = PricesProxyModel()
        self._task.set_price_model(priceProxyModel.get_price("USD_JPY"))

    def _is_condition(self):
        if settings.TEST == True:
            return True

        now = timeutils.unixtime()
        presentation_time = int(timeutils.convert_rfc2unixtime(self._task.schedule.presentation_time))
        duration = presentation_time - now
        if duration > DURATION_GET_PRICE:
            utils.info('waiting: ' + str(duration))
            return False
        elif now > presentation_time:
            raise Exception('GetPriceProcess::time is over.: ' + timeutils.format_date(now))
        return True