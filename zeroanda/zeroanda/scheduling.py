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
    # print(schedules.query)
    # print(len(schedules))

    if len(schedules) >= 1:
        for schedule in schedules:
            OrderProcess.create(schedule).run()
            # p = OrderProcess(schedule)
            # p.start()
            # model = ProcessModel(schedule=schedule, pid=333)
            # model.save()
            # i = 0
            # while i < 1:
            #     time.sleep(3)
            #     model.status=False
            #     model.save()
            #     i += 1

