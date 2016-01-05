from zeroanda.models import ScheduleModel
from zeroanda import process
from datetime import datetime, timedelta
from multiprocessing import Process

def watch_schedule():
    now = datetime.now()
    print(now)
    target_date = now + timedelta(0, 60 * 10)
    schedules = ScheduleModel.objects.filter(presentation_time__gte=now).filter(presentation_time__lte=target_date)
    print(schedules.query)
    print(len(schedules))
    if len(schedules) >= 1:
        for schedule in schedules:
            p = Process(target=process.run_process, args=(schedule,))
            p.start()
            print(p.pid)
            # p.join()

