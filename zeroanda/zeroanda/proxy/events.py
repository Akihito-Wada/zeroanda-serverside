from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class EventsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_events(self, account_id, etag = None):

        response = self._streaming.get_events(account_id, etag)
        utils.info("code: " + str(response.get_code()))
        if response.get_status():
            return response

