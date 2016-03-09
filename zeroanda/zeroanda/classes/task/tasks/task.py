from zeroanda.classes.task.interface.iprocess import IProcess
from zeroanda.classes.task.children.account_process import AccountProcess
from zeroanda.classes.task.children.price_process import PriceProcess

from zeroanda import utils

class Task(IProcess):
    __count = 0
    __process_list = []
    __target_process = None
    __schedule  = None

    __account_info_model = None
    __price_model = None

    def __init__(self, schedule):
        self.__schedule = schedule

    @staticmethod
    def create_task(schedule):
        task = Task(schedule)
        task.add_process(AccountProcess(task))
        task.add_process(PriceProcess(task))
        return task

    def exec(self):
        if self.__target_process.is_running() or self.__target_process.is_finished():
            return

        self.__target_process.exec()

    '''
    実行中のプロセスが終了していた場合は次のプロセスを取り出してセット
    実行できるプロセスがなくなったら終了
    '''
    def is_finished(self):
        utils.info("len(self.__process_list): " + str(len(self.__process_list)))
        try:
            if self.__target_process == None or self.__target_process != None and self.__target_process.is_finished():
                self.__target_process = self.__process_list.pop(0)
            utils.info(self.__target_process)
        except Exception as e:
            utils.info(e)
            return True
        else:
            return False

    def add_process(self, process):
        self.__process_list.append(process)

    def set_account_info_model(self, model):
        self.__account_info_model = model

    def set_price_model(self, model):
        utils.info(model)
        self.__price_model = model