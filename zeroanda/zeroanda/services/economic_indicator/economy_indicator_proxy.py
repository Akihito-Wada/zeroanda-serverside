from zeroanda import utils
from zeroanda.services.economic_indicator.economic_indicator_api_services import EconomicIndicatorApiServiceFactory


class EconomicIndicatorProxyModel:
    def get_latest_economic_indicator(self):
        try:
            result = EconomicIndicatorApiServiceFactory.create().get_latest_economic_indicator()
            utils.info(result.get_unique_id())
        except Exception as e:
            utils.info(e)
            return None