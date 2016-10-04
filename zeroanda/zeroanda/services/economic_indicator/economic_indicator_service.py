from zeroanda.services.economic_indicator.economic_indicator_proxy import EconomicIndicatorProxyModel
from zeroanda.services.schedule.schedule_service import ScheduleService
from zeroanda import utils

class EconomicInidcatorService:
    proxy   = None
    def __init__(self):
        self.proxy = EconomicIndicatorProxyModel()

    def add(self):
        dto = self.proxy.get_new_economic_indicator()
        if dto == None:
            return
        self.proxy.save_as_csv(dto)

        list = self.proxy.get_unique_economic_indicator_model_list(dto)

        scheduleService = ScheduleService()
        scheduleService.set_highest_priority_schedule(list)

    def create_csv_file(self):
        dto = self.proxy.get_latest_economic_indicator()
        if dto == None:
            return False
        self.proxy.save_as_csv(dto)
        return True