from zeroanda.classes.utils import timeutils
from zeroanda.proxy.streaming import Streaming
from zeroanda.models import PricesModel
from zeroanda import utils

from datetime   import datetime

class PricesProxyModel:
    _priceModel     = None
    _scheduleModel  = None
    _etag        = None

    def __init__(self, scheduleModel = None):
        self._streaming = Streaming()
        self._scheduleModel = scheduleModel

    def _add_price(self, response):
        price = response.get_body()['prices'][0]
        priceModel = PricesModel(
            ask = price['ask'],
            bid = price['bid'],
            instrument = price['instrument'],
            etag=response.get_etag(),
            time = timeutils.convert_timestamp2datetime(price['time']),
        )
        priceModel.save()
        return priceModel

    def _get_price_model(self, instruments):
        price_response = self._streaming.prices(instruments, self._priceModel)
        if self._priceModel == None or price_response.get_code() != 304:
            self._priceModel = self._add_price(price_response)
            self._etag  = price_response.get_etag()
        # elif price_response.get_code() != 304:
        #     self._priceModel = self._add_price(price_response)

    def get_price(self, instrument = None):
        if instrument != None:
            self._get_price_model(instrument)
            return self._priceModel
        elif self._scheduleModel != None:
            self._get_price_model(self._scheduleModel.country)
            return self._priceModel
        else:
            raise Exception('instrument data is required.')
