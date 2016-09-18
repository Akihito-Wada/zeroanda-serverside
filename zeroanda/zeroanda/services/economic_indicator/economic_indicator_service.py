from zeroanda.services.economic_indicator.economic_indicator_proxy import EconomicIndicatorProxyModel
from zeroanda.services.schedule.schedule_service import ScheduleService
from zeroanda import utils

class EconomicInidcatorService:
    def __init__(self): return

    def getsom(self):

        proxy = EconomicIndicatorProxyModel()
        dto = proxy.get_latest_economic_indicator()
        if dto == None:
            return
        proxy.save_as_csv(dto)

        list = proxy.get_unique_economic_indicator_model_list(dto)


        scheduleService = ScheduleService()
        scheduleService.set_highest_priority_schedule(list)
