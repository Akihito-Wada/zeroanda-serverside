from datetime import datetime, timedelta

from django import db
from django.db import IntegrityError

from zeroanda import utils
from zeroanda.classes.utils import timeutils
from zeroanda.constant import SCHEDULE_STATUS, SCHEDULE_AVAILABLE, PRIORITY, INSTRUMENTS
from zeroanda.models import ScheduleModel

class ScheduleProxyModel:
    def get_schedule(self, id = None):
        try:
            if id != None:
                return self._get_schedule_by_id(id)
            elif datetime != None:
                return self.__get_schedule_with_highest_importance()
            else:
                None
        except ScheduleModel.DoesNotExist as e:
            utils.error(e)

    def __get_schedule_with_highest_importance(self, id = None):
        try:
            now = datetime.now()
            target_startdate = now + timedelta(minutes=60)
            model = ScheduleModel.objects.filter(
                    presentation_time__lt=target_startdate,
                    presentation_time__gt=now,
                    target=SCHEDULE_AVAILABLE[0][0],
                    status=SCHEDULE_STATUS[0][0],
            ).order_by('-priority')
            if len(model) != 0:
                return model[0]
            else:
                return None
        except ScheduleModel.DoesNotExist as e:
            utils.error(e)


    def _get_schedule_by_id(self, id):
        model = ScheduleModel.objects.get(id=id)
        return model

    def _get_schedule_by_presentationdate(self):
        now = datetime.now()
        target_startdate = now + timedelta(minutes=60)
        model = ScheduleModel.objects.filter(
                presentation_time__lt=target_startdate,
                presentation_time__gt=now,
                target=SCHEDULE_AVAILABLE[0][0],
                status=SCHEDULE_STATUS[0][0],
        )
        return model

    def update_status_proceed(self, schedule):
        schedule.status = SCHEDULE_STATUS[1][0]
        db.close_old_connections()
        try:
            schedule.updated = timeutils.get_now_with_utc()
            schedule.save()
        except IntegrityError as e:
            utils.info(e)

    def update_status_complete(self, schedule):
        schedule.status = SCHEDULE_STATUS[2][0]
        db.close_old_connections()
        try:
            schedule.updated = timeutils.get_now_with_utc()
            schedule.save()
        except IntegrityError as e:
            utils.info(e)

    def add_schedule(self, title, country, presentation_time, instrument=INSTRUMENTS[0][0], priority=PRIORITY[2][0], target=SCHEDULE_AVAILABLE[0][0], status=SCHEDULE_STATUS[0][0]):
        utils.info("{title}, {country}, {instrument}, {priority}, {target}, {status}, {presentation_time}".format(title=title, country=country, instrument=instrument, priority=priority, target=target, status=status, presentation_time=presentation_time))
        model = ScheduleModel(
            title               = title,
            country             = country,
            instrument          = instrument,
            priority            = priority,
            target              = target,
            status              = status,
            presentation_time   = presentation_time
        )
        model.save()
