from zeroanda.models import ScheduleModel
from zeroanda import utils

class ScheduleProxyModel:
    def get_schedule(self, id):
        try:
            model = ScheduleModel.objects.get(id=id)
            return model
        except ScheduleModel.DoesNotExist as e:
            utils.error(e)
        # except Exception as e:
        #     utils.info(e)
