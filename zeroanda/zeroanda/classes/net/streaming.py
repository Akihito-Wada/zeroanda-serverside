"""
Demonstrates streaming feature in OANDA open api

To execute, run the following command:

python streaming.py [options]

To show heartbeat, replace [options] by -b or --displayHeartBeat
"""

import requests
import logging
from zeroanda.classes.utils.loggerutils import Logger

logger =logging.getLogger("django")

from django.conf import settings

from zeroanda.errors import ZeroandaError
from zeroanda   import utils
from zeroanda.proxy.do.requests_data_object  import RequestDataObject
from zeroanda.constant import TYPE
from zeroanda.classes.utils import timeutils

class Streaming(object):
    # _account_id = None
    _default_headers = {
        'Authorization' : 'Bearer ' + settings.TOKEN,
        'Content-type': 'application/x-www-form-urlencoded',
        'X-Accept-Datetime-Format':'unix',
        'Connection': 'keep-alive',
    }

    _compressed_headers = {
        'Authorization' : 'Bearer ' + settings.TOKEN,
        'Content-type': 'application/x-www-form-urlencoded',
        'X-Accept-Datetime-Format':'unix',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip,deflate',
    }

    _streaming_headers = {
        'Authorization' : 'Bearer ' + settings.TOKEN,
        'Content-type': 'application/x-www-form-urlencoded',
        'X-Accept-Datetime-Format':'unix',
        # 'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip,deflate',
    }

    def get_headers(self, etag=None, compressed=False):
        if etag == None:
            return self._default_headers if compressed == False else self._compressed_headers
        else:
            self._default_headers['If-None-Match'] = etag
            return self._default_headers
            # return self._default_headers.update({'If-None-Match': accountModel.etag})

    def accounts(self, etag = None):
        url = settings.DOMAIN + "/v1/accounts"
        result = self.get(url, self.get_headers(etag=etag))
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    def account_info(self, accountModel, etag = None):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id)
        result = self.get(url, self.get_headers(etag))
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    def prices(self, instruments, priceModel = None):
        url = settings.DOMAIN + "/v1/prices"
        params = {'instruments' : instruments}
        result = self.get(url, self.get_headers(None, True), params)
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    def candles(self, instrument, candleFormat = "bidask", includeFirst = "true", dailyAlignment = 21, alignmentTimezone = "America/New_York", weeklyAlignment = "Friday", granularity = None, count = 10, start = None, end = None):
        url = settings.DOMAIN + "/v1/candles"
        params = {
            'instrument' : instrument,
            'candleFormat': candleFormat,
            # 'includeFirst': includeFirst,
            'dailyAlignment': dailyAlignment,
            'alignmentTimezone': alignmentTimezone,
            'weeklyAlignment': weeklyAlignment
        }
        if granularity != None:
            params['granularity'] = granularity
        if start != None:
            params['start'] = start
        if end != None:
            params['end'] = end
        if start == None and end == None:
            params['end'] = timeutils.unixtime()

        if (start == None or end == None) and count != 0:
            params['count'] = count

        result = self.get(url, self.get_headers(None, True), params)
        return result

    '''
    ticket
    '''
    def get_trades(self, accountModel, instruments, trade_id=0, maxId=0, minId=0, count=0):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/trades"
        if trade_id != 0:
            params = {}
            url = url + "/" + str(trade_id)
            utils.info(url)
        else:
            params = {'instruments' : instruments}
            if maxId != 0:
                params["maxId"] = str(maxId)
            if minId != 0:
                params["minId"] = str(minId)
            if count != 0:
                params["count"] = str(count)
        result = self.get(url, self._compressed_headers, params)
        if result.get_status():
            return result
        else:
            raise ZeroandaError(result)

    def close_trade(self, accountModel, trade_id):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/trades/" + str(trade_id)
        result = self.delete(url, self._compressed_headers)
        if result.get_status():
            return result
        else:
            raise ZeroandaError(result)

    '''
    position
    '''
    def get_positions(self, accountModel):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/positions"
        result = self.get(url, self._compressed_headers)
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    '''
    transations
    '''
    def get_transactions(self, account_id, instrument, id = None, ids = None, count = None, max_id = None, min_id = None, etag = None):
        url = settings.DOMAIN + "/v1/accounts/" + str(account_id) + "/transactions"
        params = {}
        if id != None:
            url = url + "/" + id
        elif ids != None:
            params["ids"] = ids
        else:
            params["instrument"] = instrument

            if count != None:
                params["count"] = count
            if max_id != None:
                params["maxId"] = max_id
            if min_id != None:
                params["minId"] = min_id
        result = self.get(url, self._streaming_headers, params)
        return result
    '''
    events
    '''
    def get_events(self, account_id, etag=None):
        url = settings.DOMAIN + "/v1/events?6818465"
        # params = {'accountIds':  str(account_id)}
        result = self.get(url, self.get_headers(etag))

        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)
    '''
     未対応 status-code 405:
    '''
    def delete_positions(self, accountModel):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/positions"
        result = self.delete(url, self.get_headers())
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    '''
    orders
    '''
    def get_orders(self, account_id, instruments=None, order_id=0, max_id=0, min_id=0, count=0):
        utils.info(33333)
        url = settings.DOMAIN + "/v1/accounts/" + str(account_id) + "/orders"
        params = {}
        if order_id != 0:
            url = url + "/" + str(order_id)
        else:
            if instruments != None:
                params["instruments"] = instruments
            if max_id != 0:
                params["maxId"] = str(max_id)
            if min_id != 0:
                params["minId"] = str(min_id)
            if count != 0:
                params["count"] = str(count)

        # result = self.get(url, self.get_headers(), params)

        result = self.get(url, self._streaming_headers, params)
        return result

    def order_ifdoco(self, account_id, instruments, units, side, expiry, price, lowerBound, upperBound, takeProfit, stopLoss):
        payload = {'instrument': instruments,
                   'units': units,
                   'side': side,
                   'type': TYPE[2][0],
                   'expiry': timeutils.convert_rfc2unixtime(expiry),
                   'price': price,
                   'lowerBound': lowerBound,
                   'upperBound': upperBound,
                   'takeProfit': takeProfit,
                   'stopLoss': stopLoss
                   }
        if account_id == None:
            raise Exception('account_id is None.')
        # url = settings.STREAMING_DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/orders"
        url = settings.DOMAIN + "/v1/accounts/" + str(account_id) + "/orders"
        result = self.post(url, self.get_headers(None, True), payload)
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    def order_market(self, account_id, instruments, units, side, expiry = None, lowerBound = None, upperBound = None):

        payload = {'instrument': instruments,
                   'units': units,
                   'side': side,
                   'type': TYPE[3][0],
                   }
        if expiry != None:
            payload["expiry"] = timeutils.convert_rfc2unixtime(expiry)
        if lowerBound != None:
            payload["lowerBound"] = lowerBound
        if upperBound != None:
            payload["upperBound"] = upperBound

        if account_id == None:
            raise Exception('account_id is None.')
        # url = settings.STREAMING_DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/orders"
        url = settings.DOMAIN + "/v1/accounts/" + str(account_id) + "/orders"
        result = self.post(url, self.get_headers(None, True), payload)
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    def cancel_order(self, accountModel, actual_order_id):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/orders/" + str(actual_order_id)
        result = self.delete(url, self._compressed_headers)
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    def events(self):
        url = settings.DOMAIN + "/v1/events/"

    def calender(self, instrument, period = 2592000):
        utils.info('calender')
        utils.info(period)
        params = {
            'instrument': instrument,
            'period': period,
        }
        url = settings.DOMAIN + "/labs/v1/calendar"
        result = self.get(url, self._streaming_headers, params)
        return result

    def delete(self, url, headers, params = None):
        try:
            Logger.info("url: " + url)
            Logger.info("headers: " + str(headers))
            Logger.info("params: " + str(params))

            s = requests.Session()
            req = requests.Request('DELETE', url, headers=headers, params=params)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            if response == None:
                error = ZeroandaError()
                error.save()
                raise error
            else:
                rdo = RequestDataObject(response)
                Logger.info(rdo)
                return rdo
        except Exception as e:
            s.close()
            raise e

    def post(self, url, headers, payload):
        try:
            Logger.info("url: " + url)
            Logger.info("headers: " + str(headers))
            Logger.info("payload: " + str(payload))
            s = requests.Session()
            req = requests.Request('POST', url, headers = headers, data = payload)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            if response == None:
                error = ZeroandaError()
                error.save()
                raise error
            else:
                rdo = RequestDataObject(response)
                Logger.info(rdo)
                return rdo
        except Exception as e:
            s.close()
            raise e

    def get(self, url, headers, params = None):
        try:
            s = requests.Session()
            Logger.info("url: " + url)
            Logger.info("headers: " + str(headers))
            Logger.info("params: " + str(params))
            req = requests.Request('GET', url, headers = headers, params = params)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            if response == None:
                error = ZeroandaError()
                error.save()
                raise error
            else:
                rdo = RequestDataObject(response)
                Logger.info(rdo)
                return rdo
        except Exception as e:
            s.close()
            raise e

    def options(self, url, headers, params = None):
        try:
            s = requests.Session()
            Logger.info("url: " + url)
            Logger.info("headers: " + str(headers))
            Logger.info("params: " + str(params))
            req = requests.Request('OPTIONS', url, headers = headers, params = params)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            if response == None:
                error = ZeroandaError()
                error.save()
                raise error
            else:
                rdo = RequestDataObject(response)
                Logger.info(rdo)
                return rdo
        except Exception as e:
            s.close()
            raise e