from zeroanda.models import ScheduleModel
from zeroanda.errors import ZeroandaError
from zeroanda.process import OrderProcess
from datetime import datetime, timedelta

def watch_schedule():
    now = datetime.now()
    # print(now)
    process_start_date = now + timedelta(0, 60 * 10)
    schedules = ScheduleModel.objects.all()
        # .filter(presentation_time__gte=now).filter(presentation_time__lte=process_start_date)

    if len(schedules) >= 1:
        for schedule in schedules:
            try:
                OrderProcess.create(schedule).run()
            except ZeroandaError as e:
                print('error')
                e.save()
