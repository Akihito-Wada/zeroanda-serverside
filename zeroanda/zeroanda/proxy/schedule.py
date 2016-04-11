from zeroanda.models import ScheduleModel
from datetime import datetime, timedelta
from zeroanda import utils

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
        # except Exception as e:
        #     utils.info(e)

    def _get_schedule_by_id(self, id):
        model = ScheduleModel.objects.get(id=id)
        return model

    def _get_schedule_by_presentationdate(self):
        now = datetime.now()
        target_startdate = now + timedelta(minutes=60)
        model = ScheduleModel.objects.filter(presentation_time__lt=target_startdate,
                                     presentation_time__gt=now)
        utils.info(model.query)
        return model
