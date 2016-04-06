from zeroanda.classes.task.interface.iprocess import IProcess
from zeroanda import utils

class TickTackTask(IProcess):
    def __init__(self):pass

    @staticmethod
    def create_task():
        task = TickTackTask()
        return task

    def exec(self):
        if self.__target_process.is_runnable() == False:
            return

        self.__target_process.exec()

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