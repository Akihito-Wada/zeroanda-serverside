from django.conf import settings

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.enums.transaction_status import TransactionStatus
from zeroanda.classes.enums.process_status import ProcessStatus
from zeroanda.constant import INSTRUMENTS, UNTILE_GET_TRANSACTION_EXCUTE_TIME
from zeroanda.proxy.transactions import TransactionsProxyModel
from zeroanda import utils
from zeroanda.classes.utils import timeutils

from datetime import datetime, timedelta
from multiprocessing import Process

class GetTransactionProcess(AbstractProcess):
    def __init__(self, task):
        self._task = task
        # self._create_job()
        self._set_status(ProcessStatus.waiting)
        self.__transaction = TransactionsProxyModel()
        self.__transactions = []
        self._task.pool['count'] = 0
        # super(GetTransactionProcess, self).__init__(task)

        self._set_status(ProcessStatus.waiting)
        self._set_target_date()

    def is_runnable(self):
        result = self._get_status() == ProcessStatus.waiting
        # result = self._get_status() == ProcessStatus.waiting and self.is_running() == False
        utils.info('is_runnable: ' + str(result))
        return result

    def __reflesh(self):
        utils.info('__reflesh')
        self.__transactions = []

        self._set_status(ProcessStatus.waiting)
        # self._create_job()

    def _create_job(self):
        process = Process(target=self._get_transactions)
        self._jobs = [process]
        utils.info("self._create_job: " + str(len(self._get_job_list())))

    def exec(self):
        self._task.pool['count'] = self._task.pool['count'] + 1
        # if self._task.pool['count'] > 80:
        #     self._set_status(ProcessStatus.finish)
        #     return
        self._create_job()
        utils.info('exec')

        if self._is_condition() == False:
            return
        utils.info("self._jobs222: " + str(len(self._get_job_list())))
        if 0 == len(self._get_job_list()):
            return

        while len(self._get_job_list()) > 0:
            job = self._get_job_list().pop(0)
            utils.info(job.is_alive())
            utils.info(job.name)
            job.start()
        # for job in self._jobs:
        #     utils.info(job.is_alive())
        #     utils.info(job.name)
        #     job.start()

        self._set_status(ProcessStatus.running)

    def _get_transactions(self):
        ids = []
        ids.append(self._task.pool['actual_order_model_sell'].actual_order_id)
        ids.append(self._task.pool['actual_order_model_buy'].actual_order_id)
        etag = None if "etag" not in self._task.pool else self._task.pool["etag"]
        if etag != None:
            utils.info("etag11: " + etag)
        else:
            utils.info("etag11: nothing")
        result = self.__transaction.get_transactions(self._task.pool['account_info_model'].account_id, INSTRUMENTS[0][0], ids=",".join(map(str, ids)), etag=etag)
        self._task.pool["etag"] = result.get_etag()
        if result.get_code() == 200:
            self.__transactions.append(result.get_body()["transactions"][0])
            self.__transactions.append(result.get_body()["transactions"][1])
            utils.info(self.__transactions)
            self.__set_transaction_status()
        elif result.get_code() == 304:
            self._set_status(ProcessStatus.waiting)
            self._task.pool["etag"] = result.get_etag()
        else:
            self._set_status(ProcessStatus.finish)

    def _is_condition(self):
        now = datetime.now()
        utils.info('test1')
        utils.info(now)
        utils.info(self._target_date)
        utils.info(self._presentation_date)
        utils.info('test2')

        result = now < self._target_date
        if result == False:
            self._set_status(ProcessStatus.finish)
        return result

    def _set_target_date(self):
        self._presentation_date = self._task._presentation_date if settings.TEST else self._task.schedule.presentation_time
        self._target_date = self._presentation_date + timedelta(seconds = UNTILE_GET_TRANSACTION_EXCUTE_TIME)


    def is_finished(self):
        # return True
        # if len(self.__transactions) != 2:
        #     return False

        return self._get_status()== ProcessStatus.finish

    def __set_transaction_status(self):
        utils.info('__set_transaction_status.length: ' + str(len(self.__transactions)))
        if len(self.__transactions) != 2:
            self._set_status(ProcessStatus.running)
        else:
            tra0 = self.__transactions[0]
            tra1 = self.__transactions[1]
            utils.info(timeutils.convert_timestamp2datetime(tra0['expiry']))
            utils.info("status: " + tra0["type"] + ", " + tra1["type"])

            #running
            utils.info(str(tra0["type"] == TransactionStatus.MARKET_IF_TOUCHED_ORDER_CREATE.name))
            if tra0["type"] == TransactionStatus.MARKET_IF_TOUCHED_ORDER_CREATE.name and tra1["type"] and TransactionStatus.MARKET_IF_TOUCHED_ORDER_CREATE.name:
                self.__reflesh()
                return
            #running
            self._set_status(ProcessStatus.finish)

    def _set_status(self, status):
        utils.info("_set_status: " + status.name)
        self._task.pool["status"] = status

    def _get_status(self):
        if "status" not in self._task.pool :
            self._set_status(ProcessStatus.waiting)
        return self._task.pool["status"]

    def _get_job_list(self):
        return self._jobs
