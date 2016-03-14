from zeroanda.classes.task.tasks.task import Task
from zeroanda.classes.task.tick_tack import TickTack
from zeroanda.models import ScheduleModel
from zeroanda import utils

class Action:
    tmp = {}
    def __init__(self):
        self.__createTask()

    def __createTask(self):pass

    def WatchSchedule(self):
        schedule = 3
        schedules = ScheduleModel.objects.all()[:1]
        self.startTickTack(schedules[0])

    def startTickTack(self, schedule):
        tickTack = TickTack()
        tickTack.tickTack(Task.create_task(schedule))
