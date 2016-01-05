from django.core.management.base import BaseCommand, CommandError
from zeroanda import scheduling
import logging

logger =logging.getLogger("django")

class Command(BaseCommand):
    help = 'excute process.'
    def handle(self, *args, **options):
        scheduling.watch_schedule()

        # now = datetime.now()
        # target_date = now + timedelta(0, 60 * 10)
        # schedules = ScheduleModel.objects.filter(presentation_time__gte=now).filter(presentation_time__lte=target_date)
        # print(schedules.query)
        # print(schedules)

        # streaming.demo(True)
        # i = 0
        # while i < 3:
        #     streaming.get_prices()
        #     time.sleep(local_settings.WAIT_TIME)
        #     i += 1