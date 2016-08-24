from zeroanda.constant import SIDE, TYPE, ACTUAL_ORDER_STATUS, INSTRUMENTS, ERROR_CODE, ORDER_STATUS
from zeroanda.errors import ZeroandaError
from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class TradesProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_trades(self, accountModel):
        result = self._streaming.get_trades(accountModel, INSTRUMENTS[0][0])
        return result.get_body()

    def close_trades(self, accountModel, trade_id):
        result = self._streaming.close_trade(accountModel, trade_id)

    def close_all_trades(self, accountModel):
        try :
            result = self.get_trades(accountModel)

            if 'trades' in result:
                for trade in result['trades']:
                    self.close_trades(accountModel, trade['id'])
        except Exception as e:
            print(e)
