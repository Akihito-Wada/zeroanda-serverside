from zeroanda.classes.task.interface.iprocess import IProcess
from zeroanda.classes.task.children.get_account_process import GetAccountProcess
from zeroanda.classes.task.children.get_price_process import GetPriceProcess
from zeroanda.classes.task.children.set_unit_process import SetUnitProcess

from zeroanda import utils

class Task(IProcess):
    _process_list = []
    __target_process = None
    __schedule  = None

    account_info_model = None
    _price_model = None
    pool = {}

    def __init__(self, schedule):
        self.__schedule = schedule

    @staticmethod
    def create_task(schedule):
        task = Task(schedule)
        task.add_process(GetAccountProcess(task))
        task.add_process(GetPriceProcess(task))
        task.add_process(SetUnitProcess(task))
        return task

    def exec(self):
        # if self.__target_process.is_running() or self.__target_process.is_finished():
        #     return

        self.__target_process.exec()

    '''
    実行中のプロセスが終了していた場合は次のプロセスを取り出してセット
    実行できるプロセスがなくなったら終了
    '''
    def is_finished(self):

        utils.info("len(self.__process_list): " + str(len(self._process_list)))
        try:
            if self.__target_process == None or self.__target_process != None and self.__target_process.is_finished():
                self.__target_process = self._process_list.pop(0)
            utils.info(self.__target_process)
        except Exception as e:
            utils.info(e)
            return True
        else:
            return False

    def add_process(self, process):
        self._process_list.append(process)

    def set_account_info_model(self, model):
        self.account_info_model = model

    def set_price_model(self, model):
        self._price_model = model

