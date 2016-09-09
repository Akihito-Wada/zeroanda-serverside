from zeroanda   import utils
from zeroanda.classes.net.streaming import Streaming


class PositionsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_positions(self, accountModel):
        result = self._streaming.get_positions(accountModel)
        utils.info(result.get_body())

    def delete_positions(self, accountModel):
        result = self._streaming.delete_positions(accountModel)
        utils.info(result.get_body())