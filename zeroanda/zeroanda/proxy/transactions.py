from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class TransactionsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_transactions(self, account_id, instrument, count = None):
        response = self._streaming.get_transactions(account_id, instrument, count)
        utils.info(response.get_code())
        if response.get_code() == 200:
            return response.get_body()