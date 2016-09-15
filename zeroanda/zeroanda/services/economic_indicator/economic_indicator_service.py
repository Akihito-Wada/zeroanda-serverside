from zeroanda.proxy.schedule import ScheduleProxyModel
from zeroanda.services.economic_indicator.economic_indicator_proxy import EconomicIndicatorProxyModel
from zeroanda import utils

class EconomicInidcatorService:
    def __init__(self): return

    def getsom(self):

        proxy = EconomicIndicatorProxyModel()
        dto = proxy.get_latest_economic_indicator()

        proxy.save_as_csv(dto)

        list = proxy.get_unique_economic_indicator_model_list(13, dto)
        scheduleProxy = ScheduleProxyModel()
        scheduleProxy.set_highest_priority_schedule(list)
        #
        #
        # scheduleProxyModel = ScheduleProxyModel()
        # scheduleProxyModel.set_highest_priority_schedule(dto)