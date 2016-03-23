from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.enums.transaction_status import TransactionStatus
from zeroanda.classes.enums.process_status import ProcessStatus
from zeroanda.constant import INSTRUMENTS
from zeroanda.proxy.transactions import TransactionsProxyModel
from zeroanda import utils
from multiprocessing import Process

class GetTransactionProcess(AbstractProcess):
    def __init__(self, task):
        self._task = task
        # self._create_job()
        self._set_status(ProcessStatus.waiting)
        self.__transaction = TransactionsProxyModel()
        self.__transactions = []

        # super(GetTransactionProcess, self).__init__(task)

        self._set_status(ProcessStatus.waiting)

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
        result = self.__transaction.get_transactions(self._task.pool['account_info_model'].account_id, INSTRUMENTS[0][0], ",".join(map(str, ids)))

        self.__transactions.append(result["transactions"][0])
        self.__transactions.append(result["transactions"][1])
        utils.info(self.__transactions)
        self.__set_transaction_status()

    def _is_condition(self):
        return True

    def is_finished(self):
        # return True
        if len(self.__transactions) != 2:
            return False

        return self._get_status()== ProcessStatus.finish

    def __set_transaction_status(self):
        utils.info('__set_transaction_status.length: ' + str(len(self.__transactions)))
        if len(self.__transactions) != 2:
            self._set_status(ProcessStatus.running)
        else:
            tra0 = self.__transactions[0]
            tra1 = self.__transactions[1]
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
