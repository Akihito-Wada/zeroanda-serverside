from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.enums.transaction_status import TransactionStatus
from zeroanda.classes.enums.process_status import ProcessStatus
from zeroanda.constant import INSTRUMENTS
from zeroanda.proxy.transactions import TransactionsProxyModel
from zeroanda import utils
from multiprocessing import Process

class GetTransactionProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        self.__transaction = TransactionsProxyModel()
        self.__transactions = []
        self._set_status(ProcessStatus.waiting)
        super(GetTransactionProcess, self).__init__(task)

    def is_runnable(self):
        result = self._get_status() == ProcessStatus.waiting and self.is_running() == False
        utils.info("GetTransactionProcess.self.get_status(): " + self._get_status().name + ", self.is_running(): " + str(self.is_running()))
        utils.info('is_runnable: ' + str(result))
        return result

    def __reflesh(self):
        utils.info('__reflesh')
        self.__transactions = []
        self._set_status(ProcessStatus.waiting)
        self._create_job()

    def _create_job(self):
        self._jobs.append(Process(target=self._get_transactions))

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
        if len(self.__transactions) != 2:
            self._set_status(ProcessStatus.running)
        else:
            tra0 = self.__transactions[0]
            tra1 = self.__transactions[1]
            utils.info("status: " + tra0["type"] + ", " + tra1["type"])

            # finish
            # 1 or 2 transaction(s) have closed.
            # if tra0["type"] == TransactionStatus.TRADE_CLOSE.name or tra1["type"] == TransactionStatus.TRADE_CLOSE.name:
            #     self.status = ProcessStatus.finish
            #     return

            # both of transactions have expired.
            # if tra0["type"] == TransactionStatus.ORDER_CANCEL.name or tra1["type"] and TransactionStatus.ORDER_CANCEL.name:
            #     self.status = ProcessStatus.finish
            #     return
            # finish

            #running
            utils.info(str(tra0["type"] == TransactionStatus.MARKET_IF_TOUCHED_ORDER_CREATE.name))
            if tra0["type"] == TransactionStatus.MARKET_IF_TOUCHED_ORDER_CREATE.name and tra1["type"] and TransactionStatus.MARKET_IF_TOUCHED_ORDER_CREATE.name:
                self.__reflesh()
                utils.info("self.status.name: " + self.status.name)
                return
            #running
            self._set_status(ProcessStatus.finish)

            # for transaction in self.__transactions:
            #     utils.info(transaction["type"] != TransactionStatus.ORDER_CANCEL.name)
            #     if transaction["type"] != TransactionStatus.ORDER_CANCEL.name:
            #         return
            #     if transaction["type"] == TransactionStatus.TRADE_CLOSE.name:
            #         self.status = ProcessStatus.finish
            #         return
            # self.status = ProcessStatus.waiting
