from zeroanda.models import ScheduleModel, ProcessModel
from zeroanda.process import OrderProcess
from datetime import datetime, timedelta
from multiprocessing import Process
import  time

def watch_schedule():
    now = datetime.now()
    # print(now)
    process_start_date = now + timedelta(0, 60 * 10)
    schedules = ScheduleModel.objects.all()
        # .filter(presentation_time__gte=now).filter(presentation_time__lte=process_start_date)

    if len(schedules) >= 1:
        for schedule in schedules:
            OrderProcess.create(schedule).run()
