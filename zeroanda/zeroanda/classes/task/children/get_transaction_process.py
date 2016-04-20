from django import db
from django.conf import settings

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.enums.transaction_status import TransactionStatus
from zeroanda.classes.enums.process_status import ProcessStatus
from zeroanda.constant import INSTRUMENTS
from zeroanda.models import TradeTransactionModel
from zeroanda.proxy.transactions import TransactionsProxyModel
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
        instrument = INSTRUMENTS[0][0] if settings.TEST else self._task.schedule.country
        result = transactionProxyModel.get_transactions(account_id=self._task.pool["account_info_model"].account_id, instrument=instrument, count=2)

        if result.get_code() == 429:
            return
        if 'transactions' not in result.get_body():
            transaction = result.get_body()
            if "side" in transaction:
                key = "actual_order_model_" + transaction['side']
                actual_order_model = None if key not in self._task.pool else self._task.pool[key]
                transactionProxyModel.add(transaction,schedule=self._task.schedule,trade_id=self._task.pool['trade_id'], actual_order_model=actual_order_model)
        else:
            transactions = result.get_body()["transactions"]
            for transaction in transactions:
                if "side" in transaction:
                    key = "actual_order_model_" + transaction['side']
                    actual_order_model = None if key not in self._task.pool else self._task.pool[key]
                    transactionProxyModel.add(transaction, schedule=self._task.schedule, trade_id=self._task.pool['trade_id'], actual_order_model=actual_order_model)

    def _is_condition(self):
        now = timeutils.get_now_with_jst()
        utils.info(self.__class__.__name__ + "::_is_condition::now: " + str(now) + ", target_date: " + str(self._target_date))
        result = now > self._target_date
        if result == True:
            db.close_old_connections()
            self.__transaction_model.excute_time = timeutils.get_now_with_jst()
            self.__transaction_model.save()
        return result

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        self._target_date = self._presentation_date + timedelta(seconds = settings.GET_TRANSACTION_EXCUTE_TIME)

        self.__transaction_model = TradeTransactionModel(trade_model=self._task.trade_model, presentation_time=self._target_date,
                                                    transaction_name=self.__class__.__name__)
        self.__transaction_model.save()

