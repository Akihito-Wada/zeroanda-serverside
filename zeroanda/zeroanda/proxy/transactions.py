from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class TransactionsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_transactions(self, account_id, instrument, ids = None, count = None, etag = None):
        if etag == None:
            utils.info("none")

        response = self._streaming.get_transactions(account_id, instrument, ids=ids, count=count, etag=etag)
        utils.info("code: " + str(response.get_code()))
        if response.get_status():
            return response
        # if response.get_code() == 200 or response.get_code() == 304 :
        #     return response
            # return response.get_body()
