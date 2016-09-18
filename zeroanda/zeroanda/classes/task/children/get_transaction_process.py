from django import db
from django.conf import settings

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.utils.loggerutils import Logger
from zeroanda.constant import INSTRUMENTS
from zeroanda.controller.mail_manager import MailManager
from zeroanda.models import TradeTransactionModel
from zeroanda.proxy.setting import SettingProxy
from zeroanda.proxy.transactions import TransactionsProxyModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda import utils
from zeroanda.classes.utils import timeutils

from datetime import timedelta
from multiprocessing import Process

class GetTransactionProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(GetTransactionProcess, self).__init__(task)

        self._set_target_date()

    def _create_job(self):
        self._jobs.append(Process(target=self._get_transactions))

    def _get_transactions(self):
        transactionProxyModel = TransactionsProxyModel()
        instrument = INSTRUMENTS[0][0] if settings.TEST else self._task.schedule.instrument
        result = transactionProxyModel.get_transactions(account_id=self._task.pool["account_info_model"].account_id, instrument=instrument, count=2)
        
        orderProxy = OrderProxyModel()
        if result.get_code() == 429:
            return
        if 'transactions' not in result.get_body():
            transaction = result.get_body()
            actual_order_model = orderProxy.get_actual_order_model(actual_order_id=transaction["orderId"])
            transactionProxyModel.add(transaction,schedule=self._task.schedule,trade_id=self._task.pool['trade_id'], actual_order_model=actual_order_model)
        else:
            transactions = result.get_body()["transactions"]
            for transaction in transactions:
                actual_order_model = orderProxy.get_actual_order_model(actual_order_id=transaction["orderId"])
                transactionProxyModel.add(transaction, schedule=self._task.schedule, trade_id=self._task.pool['trade_id'],actual_order_model=actual_order_model)

        # MailManager.send_finish_mail(self._task.schedule)

    def _is_condition(self):
        now = timeutils.get_now_with_jst()
        Logger.info(self.__class__.__name__ + "::_is_condition::now: " + str(now) + ", target_date: " + str(self._target_date))
        result = now > self._target_date
        if result == True:
            db.close_old_connections()
            self.__transaction_model.excute_time = timeutils.get_now_with_jst()
            self.__transaction_model.save()
        return result

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        # self._target_date = self._presentation_date + timedelta(seconds = settings.GET_TRANSACTION_EXCUTE_TIME)
        self._target_date = self._presentation_date + timedelta(seconds=SettingProxy.get_transaction_excute_time(self._get_priority()))
        self.__transaction_model = TradeTransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date,
                                                    transaction_name=self.__class__.__name__)
        self.__transaction_model.save()

