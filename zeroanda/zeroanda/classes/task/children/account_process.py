from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.proxy.account import AccountProxyModel

from zeroanda import utils

import time

class AccountProcess(AbstractProcess):
    __task      = None

    def _exec(self):
        accountProxyModel = AccountProxyModel()
        self._task.set_account_info_model(accountProxyModel.get_account_info())
        # utils.info(211)
        # time.sleep(5)
        # utils.info(213)
