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
        utils.info(result.get_body())

    def close_trades(self, accountModel, trade_id):
        result = self._streaming.close_trade(accountModel, trade_id)
        utils.info(result.get_body())