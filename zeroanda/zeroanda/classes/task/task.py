from zeroanda.classes.task.status import ProcessStatus

class Task:
    __processList = []
    __status    = ProcessStatus.UNEXECUTED

    def __init__(self):
        return

    def addProcess(self, process):
        self.__processList.append(process)

    def hasProcess(self):
        process = self.__processList.pop(0)