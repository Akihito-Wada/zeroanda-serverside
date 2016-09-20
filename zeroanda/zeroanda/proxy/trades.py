from zeroanda.classes.net.streaming import Streaming
from zeroanda.constant import INSTRUMENTS


class TradesProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_trades(self, accountModel, trade_id=0, maxId = 0, minId=0, count=0):
        result = self._streaming.get_trades(accountModel, INSTRUMENTS[0][0], trade_id, maxId, minId, count)
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
