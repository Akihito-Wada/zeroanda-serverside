from zeroanda.classes.utils import timeutils
from zeroanda.proxy.schedule import ScheduleProxyModel
from zeroanda.proxy.priority import PriorityProxyModel
from zeroanda.services.country.country_proxy import CountryProxyModel
from zeroanda   import utils

class ScheduleService:
    def __init__(self):return


    def set_highest_priority_schedule(self, list):
        try:
            scheduleProxy   = ScheduleProxyModel()
            countryProxy    = CountryProxyModel()
            for item in list:
                scheduleProxy.add_schedule(
                    title=item.event,
                    country=countryProxy.get_index(item.currency),
                    priority=PriorityProxyModel.convert_prioriy(item.importance),
                    presentation_time=timeutils.convert_aware_datetime_from_utc_to_jst(item.date)
                )
        except Exception as e:
            utils.info(e)