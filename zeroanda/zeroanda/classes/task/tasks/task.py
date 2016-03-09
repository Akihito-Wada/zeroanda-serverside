from zeroanda.classes.task.status import ProcessStatus
from zeroanda.classes.task.interface.iprocess import IProcess
from zeroanda import utils

class Task(IProcess):
    __targetProcess = None
    __schedule  = None
    __status    = ProcessStatus.UNEXECUTED

    def __init__(self, schedule):
        self.__schedule = schedule

    @staticmethod
    def createTask(schedule):
        task = Task(schedule)
        # task.addProcess()
        return task

    def exec(self):
        self.__targetProcess.exec()

    def isFinished(self):
        return self.__status == ProcessStatus.FINISH

    def addProcess(self, process):
        if self.__targetProcess == None:
            self.__targetProcess = process
        else:
            self.__targetProcess.addProcess(process)

    def hasProcess(self):
        return self.__targetProcess != None or self.__targetProcess.status == ProcessStatus.FINISH
        # try:
        #     process = self.__processList.pop(0)
        #     utils.info(process)
        #     for process in range(len(self.__processList)):
        #         process.isFinished()
        #         break
        #     while (True):
        #         if process.isFinished():
        #             process = process.next()
        #         process.exec()
        #
        # except Exception as e:
        #     utils.error(e)
        #     return False

