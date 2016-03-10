from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.proxy.account import AccountProxyModel
from zeroanda import utils
from multiprocessing import Process

class GetAccountProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        super(GetAccountProcess, self).__init__(task)

    def _create_job(self):
        self._jobs.append(Process(target=self._get_account))

    def _get_account(self):
        accountProxyModel = AccountProxyModel()
        accountProxyModel.get_account_info()
        self._task.set_account_info_model(accountProxyModel.get_account_info())

    def _is_condition(self):
        return True
