from django import db
from django.conf import settings
from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.utils import timeutils
from zeroanda.classes.utils.loggerutils import Logger
from zeroanda.constant import INSTRUMENTS
from zeroanda.models import TradeTransactionModel
from zeroanda.proxy.prices import PricesProxyModel

from datetime import timedelta
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
        instrument = INSTRUMENTS[0][0] if settings.TEST else self._task.schedule.instrument
        self._task.set_price_model(priceProxyModel.get_price(instrument=instrument, trade_id=self._task.pool['trade_id']))

    def _is_condition(self):
        now = timeutils.get_now_with_jst()
        Logger.info(self.__class__.__name__ + "::_is_condition::now: " + str(now) + ", target_date: " + str(self._target_date))
        if now > self._presentation_date:
            raise Exception('IfdococProcess::presentation time has already passed.')
        result = now > self._target_date
        if result == True:
            db.close_old_connections()
            self.__transaction_model.excute_time = now
            self.__transaction_model.save()
        return result

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        self._target_date = self._presentation_date + timedelta(seconds = settings.DURATION_GET_PRICE_EXCUTE_TIME)

        self.__transaction_model = TradeTransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date, transaction_name=self.__class__.__name__)
        self.__transaction_model.save()


class GetPriceProcessContinuously(GetPriceProcess):
    def __init__(self):
        self._jobs = []
        self._set_target_date()

        super(GetPriceProcessContinuously, self).__init__()

    def _is_condition(self):
        now = timeutils.get_now_with_jst()
        if now > self._presentation_date:
            raise Exception('IfdococProcess::presentation time has already passed.')
        result = now > self._target_date
        if result == True:
            db.close_old_connections()
            self.__transaction_model.excute_time = now
            self.__transaction_model.save()
        return result

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        self._target_date = self._presentation_date + timedelta(seconds = settings.DURATION_GET_PRICE_EXCUTE_TIME)
        self.__transaction_model = TradeTransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date, transaction_name=self.__class__.__name__)
        self.__transaction_model.save()