from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.constant import INSTRUMENTS
from zeroanda.proxy.transactions import TransactionsProxyModel
from zeroanda import utils
from multiprocessing import Process

class GetTransactionProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        self.__transaction = TransactionsProxyModel()
        super(GetTransactionProcess, self).__init__(task)

    def _create_job(self):
        self._jobs.append(Process(target=self._get_transactions))

    def _get_transactions(self):
        result = self.__transaction.get_transactions(self._task.pool['account_info_model'].account_id, INSTRUMENTS[0][0], 2)
        utils.info(result)

    def _is_condition(self):
        return True
