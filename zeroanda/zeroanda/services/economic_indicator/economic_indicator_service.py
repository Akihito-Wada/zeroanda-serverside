from zeroanda.services.economic_indicator.economic_indicator_proxy import EconomicIndicatorProxyModel

class EconomicInidcatorService:
    def __init__(self): return

    def getsom(self):
        proxy = EconomicIndicatorProxyModel()
        proxy.get_latest_economic_indicator()