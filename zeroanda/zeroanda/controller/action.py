from zeroanda.classes.task.tasks.task import Task
from zeroanda.classes.task.tick_tack import TickTack
from zeroanda import utils

class Action:
    def __init__(self):
        self.__createTask()

    def __createTask(self):pass

    def WatchSchedule(self):
        schedule = 3
        self.startTickTack(schedule)

    def startTickTack(self, schedule):
        tickTack = TickTack()
        tickTack.tickTack(Task.create_task(schedule))