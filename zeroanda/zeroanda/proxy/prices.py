from zeroanda.classes.utils import timeutils
from zeroanda.proxy.streaming import Streaming
from zeroanda.models import PricesModel
from zeroanda import utils

from datetime   import datetime

class PricesProxyModel:
    _priceModel     = None
    _scheduleModel  = None
    _etag        = None
    __trade_id   = 0

    def __init__(self):
        self._streaming = Streaming()

    def _add_price(self, response):
        price = response.get_body()['prices'][0]
        priceModel = PricesModel(
            ask = price['ask'],
            bid = price['bid'],
            instrument = price['instrument'],
            etag=response.get_etag(),
            time = timeutils.convert_timestamp2datetime(price['time']),
            trade_id=self.__trade_id
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

    def get_price(self, instrument = None, trade_id=0):
        self.__trade_id = trade_id

        if instrument != None:
            self._get_price_model(instrument)
            return self._priceModel

        elif trade_id != None:
            try:
                return PricesModel.objects.get(trade_id=trade_id)
            except PricesModel.DoesNotExist:
                return None

        else:
            raise Exception('instrument data is required.')

    def get_candles(self, instrument, start = None, end = None, count = 20):
        response = self._streaming.candles(instrument, start=start, end=end, count=count)
        # utils.info(response.get_body())
        return response.get_body()
