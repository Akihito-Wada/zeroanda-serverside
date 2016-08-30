from zeroanda.proxy.schedule import ScheduleProxyModel
from zeroanda.controller.mail_manager import MailManager
from zeroanda.classes.task.tasks.task import Task
from zeroanda.classes.task.tick_tack import TickTack
from zeroanda.classes.utils.loggerutils import Logger
from zeroanda import utils

class Action:
    def __init__(self):
        self.__proxy = ScheduleProxyModel()
    def WatchSchedule(self):
        schedules = self.__proxy.get_schedule()
        utils.info(len(schedules))
        if len(schedules) > 0:
            Logger.setLogFileNameBySchedule(schedules[0])
            self.__proxy.update_status_proceed(schedules[0])
            self.startTickTack(schedules[0])

    def startTickTack(self, schedule):
        # MailManager.send_opening_mail(schedule)
        # MailManager.send_mail_test()

        tickTack = TickTack()
        tickTack.tickTack(Task.create_task(schedule))

        self.__proxy.update_status_complete(schedule)
