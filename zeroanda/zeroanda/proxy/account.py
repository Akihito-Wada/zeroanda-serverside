from zeroanda.models import AccountModel
from zeroanda.proxy.streaming import Streaming

class AccountProxyModel:
    accountModel = None
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_account(self):
        result = self._streaming.accounts()
        result = self._streaming.accounts(result['accounts'][0]['accountId'])
        self.accountModel = AccountModel(
                            account_id = result['accountId'],
                            margin_rate = result['marginRate'],
                            account_currency = result['accountCurrency'],
                            account_name = result['accountName'],
                            balance    = result['balance'],
                            open_orders= result['openOrders'],
                            open_trades= result['openTrades'],
                            unrealized_pl= result['unrealizedPl'],
                            realized_pl= result['realizedPl'],
                            margin_avail= result['marginAvail'],
                            margin_used= result['marginUsed'],
        )
        self.accountModel.save()
        return self.accountModel