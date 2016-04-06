from django.conf import settings
from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.constant import DURATION_GET_PRICE_EXCUTE_TIME
from zeroanda.models import TransactionModel
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda import utils

from datetime import datetime, timedelta
from multiprocessing import Process

class GetPriceProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(GetPriceProcess, self).__init__(task)

        self._set_target_date()

    def _create_job(self):
        self._jobs.append(Process(target=self._get_price))

    def _get_price(self):
        priceProxyModel = PricesProxyModel()
        self._task.set_price_model(priceProxyModel.get_price("USD_JPY"))

    # def _is_condition(self):
    #     if settings.TEST == True:
    #         return True
    #
    #     now = timeutils.unixtime()
    #     presentation_time = int(timeutils.convert_rfc2unixtime(self._task.schedule.presentation_time))
    #     duration = presentation_time - now
    #     if duration > DURATION_GET_PRICE:
    #         utils.info('waiting: ' + str(duration))
    #         return False
    #     elif now > presentation_time:
    #         raise Exception('GetPriceProcess::time is over.: ' + timeutils.format_date(now))
    #     return True

    def _is_condition(self):
        now = datetime.now()
        if now > self._presentation_date:
            raise Exception('IfdococProcess::presentation time has already passed.')
        result = now > self._target_date
        if result == True:
            self.__transaction_model.excute_time = datetime.now()
            self.__transaction_model.save()
        return result

    def _set_target_date(self):
        # self._presentation_date = datetime.now() + timedelta(seconds = 70) if settings.TEST else self._task.schedule.presentation_time
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        self._target_date = self._presentation_date + timedelta(seconds = DURATION_GET_PRICE_EXCUTE_TIME)

        self.__transaction_model = TransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date, transaction_name=self.__class__.__name__)
        self.__transaction_model.save()


class GetPriceProcessContinuously(GetPriceProcess):
    def __init__(self):
        self._jobs = []
        self._set_target_date()

        super(GetPriceProcessContinuously, self).__init__()

    def _is_condition(self):
        now = datetime.now()
        if now > self._presentation_date:
            raise Exception('IfdococProcess::presentation time has already passed.')
        result = now > self._target_date
        if result == True:
            self.__transaction_model.excute_time = datetime.now()
            self.__transaction_model.save()
        return result


    def _set_target_date(self):
        # self._presentation_date = datetime.now() + timedelta(seconds = 70) if settings.TEST else self._task.schedule.presentation_time
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        self._target_date = self._presentation_date + timedelta(seconds = DURATION_GET_PRICE_EXCUTE_TIME)

        self.__transaction_model = TransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date, transaction_name=self.__class__.__name__)
        self.__transaction_model.save()