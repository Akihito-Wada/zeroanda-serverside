from zeroanda.constant import SIDE, TYPE, ACTUAL_ORDER_STATUS, INSTRUMENTS, ERROR_CODE, ORDER_STATUS
from zeroanda.errors import ZeroandaError
from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class TradesProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def traders(self, accountModel):
        self._streaming.traders(accountModel, INSTRUMENTS[0][0])