from zeroanda.proxy.schedule import ScheduleProxyModel
from zeroanda.controller.mail_manager import MailManager
from zeroanda.classes.task.tasks.task import Task
from zeroanda.classes.task.tick_tack import TickTack
from zeroanda.models import ScheduleModel
from zeroanda import utils

class Action:

    def WatchSchedule(self):
        proxy = ScheduleProxyModel()
        schedules = proxy.get_schedule()

        if len(schedules) > 0:
            self.startTickTack(schedules[0])
            proxy.set_status_proceed(schedules[0])

    def startTickTack(self, schedule):
        MailManager.send_opening_mail(schedule)

        # tickTack = TickTack()
        # tickTack.tickTack(Task.create_task(schedule))

class TickTackPriceAction:
    def tick_tack(self):
        tickTack = TickTack()