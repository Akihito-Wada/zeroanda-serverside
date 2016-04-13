from zeroanda.classes.task.interface.iprocess import IProcess
from zeroanda.classes.task.children.get_account_process import GetAccountProcess
from zeroanda.classes.task.children.get_order_process import GetOrderProcess
from zeroanda.classes.task.children.get_price_process import GetPriceProcess
from zeroanda.classes.task.children.set_unit_process import SetUnitProcess
from zeroanda.classes.task.children.ifdococ_process import IfdococProcess
from zeroanda.classes.task.children.get_transaction_process import GetTransactionProcess
from zeroanda import utils
from zeroanda.classes.utils import timeutils
from zeroanda.models import TradeModel

from django.conf import settings

from datetime import timedelta
from multiprocessing import Manager

class Task(IProcess):
    _process_list = []
    __target_process = None
    schedule  = None

    def __init__(self, schedule):
        self.schedule = schedule
        manager = Manager()
        self.pool = manager.dict()
        self._presentation_date = timeutils.get_now_with_jst() + timedelta(seconds = 70) if settings.TEST else timeutils.convert_aware_datetime_from_utc_to_jst(self.schedule.presentation_time)
        self.trade_model = TradeModel(schedule=schedule, presentation_time=self._presentation_date, created=timeutils.get_now_with_utc())
        self.trade_model.save()

    @staticmethod
    def create_task(schedule):
        task = Task(schedule)
        task.add_process(GetAccountProcess(task))
        task.add_process(GetPriceProcess(task))
        task.add_process(SetUnitProcess(task))
        task.add_process(IfdococProcess(task))
        # task.add_process(GetTransactionProcess(task))
        return task

    def exec(self):
        if self.__target_process.is_runnable() == False:
            return
        # if self.__target_process.is_running() or self.__target_process.is_finished():
        #     return

        self.__target_process.exec()

    '''
    実行中のプロセスが終了していた場合は次のプロセスを取り出してセット
    実行できるプロセスがなくなったら終了
    '''
    def is_finished(self):

        utils.info("len(self.__process_list): " + str(len(self._process_list)))
        utils.info("self.__target_process: " + str(self.__target_process) if self.__target_process != None else "None")
        try:
            if self.__target_process == None or self.__target_process != None and self.__target_process.is_finished():
                self.__target_process = self._process_list.pop(0)
                utils.info('poped.')
            utils.info(self.__target_process)
        except Exception as e:
            utils.info(e)
            return True
        else:
            return False

    def add_process(self, process):
        self._process_list.append(process)

    def set_account_info_model(self, model):
        self.pool["account_info_model"] = model

    def set_price_model(self, model):
        self.pool["price_model"] = model

    def set_orders_model(self, model):
        self.pool["orders_model"] = model

    def set_actual_orders_model(self, side, model):
        self.pool["actual_order_model_" + side] = model