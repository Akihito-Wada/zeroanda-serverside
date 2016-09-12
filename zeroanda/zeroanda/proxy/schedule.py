from zeroanda.proxy.service.http_service import HttpService
from zeroanda.classes.utils import timeutils
from zeroanda.classes.utils.loggerutils import Logger
from zeroanda.constant import SCHEDULE_STATUS, SCHEDULE_AVAILABLE
from zeroanda.models import ScheduleModel
from zeroanda import utils

from django.db import IntegrityError
from django import db

from datetime import datetime, timedelta

class ScheduleProxyModel:
    def get_schedule(self, id = None):
        try:
            if id != None:
                return self._get_schedule_by_id(id)
            elif datetime != None:
                return self._get_schedule_by_presentationdate()
            else:
                None
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

    def get_economic_indicator(self):
        try:
            result = HttpService.create().get_latest_economic_indicator()
        except Exception as e:
            utils.info(e)
            return None