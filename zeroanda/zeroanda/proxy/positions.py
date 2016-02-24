from zeroanda.constant import SIDE, TYPE, ACTUAL_ORDER_STATUS, INSTRUMENTS, ERROR_CODE, ORDER_STATUS
from zeroanda.errors import ZeroandaError
from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class PositionsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_positions(self, accountModel):
        result = self._streaming.get_positions(accountModel)
        utils.info(result.get_body())

    # def delete_positions(self, accountModel):
    #     result = self._streaming.delete_positions(accountModel)
    #     utils.info(result.get_body())