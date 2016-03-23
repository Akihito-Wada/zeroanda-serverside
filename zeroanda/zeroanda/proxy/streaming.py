"""
Demonstrates streaming feature in OANDA open api

To execute, run the following command:

python streaming.py [options]

To show heartbeat, replace [options] by -b or --displayHeartBeat
"""

import requests
import json
import logging

logger =logging.getLogger("django")

from optparse import OptionParser
from django.conf import settings

#
# def connect_to_stream(url):
#     """
#
#     Environment           <Domain>
#     fxTrade               stream-fxtrade.oanda.com
#     fxTrade Practice      stream-fxpractice.oanda.com
#     sandbox               stream-sandbox.oanda.com
#     """
#
#     # Replace the following variables with your personal ones
#     # domain = 'stream-fxpractice.oanda.com'
#     # domain = 'api-sandbox.oanda.com'
#     # access_token = 'ACCESS-TOKEN'
#     # account_id = '1234567'
#     # instruments = "EUR_USD,USD_CAD"
#
#     try:
#         s = requests.Session()
#         # url = "https://" + domain + "/v1/prices"
#         headers = {'Authorization' : 'Bearer ' + settings.TOKEN,
#                    'Content-type': 'application/x-www-form-urlencoded',
#                    'X-Accept-Datetime-Format':'unix',
#                    'Connection': 'keep-alive',
#                    'Accept-Encoding': 'gzip,deflate',
#                   }
#         # params = {'instruments' : instruments, 'accountId' : account_id}
#         params = {'instruments' : ','.join(settings.INSTRUMENTS)}
#         req = requests.Request('GET', url, headers = headers, params = params)
#         pre = req.prepare()
#         resp = s.send(pre, stream = True, verify = False)
#         return resp
#     except Exception as e:
#         s.close()
#
#         print("Caught exception when connecting to stream\n" + str(e))
#
# def demo(displayHeartbeat):
#     url = "http://" + settings.DOMAIN + "/v1/prices"
#     response = connect_to_stream(url)
#     if response.status_code != 200:
#         print(response.text)
#         return
#     test = json.loads(response.text)
#     # print(test["prices"][0]["instrument"])
#     print(test["prices"])
#     # print(datetime.datetime.fromtimestamp(int(test["prices"][0]["time"])))
#     # for line in response.iter_lines(1):
#     #     if line:
#     #         try:
#     #             print(line)
#     #             msg = json.loads(line)
#     #         except Exception as e:
#     #             print("Caught exception when converting message into json\n" + str(e))
#     #             return
#     #
#     #         if displayHeartbeat:
#     #             print(line)
#     #         else:
#     #             if msg.has_key("instrument") or msg.has_key("tick"):
#     #                 print(line)
#
# def get_prices():
#     utils.info("prices")
#     url = settings.DOMAIN + "/v1/prices"
#     response = connect_to_stream(url)
#     if response.status_code != 200:
#         print(response.text)
#         return
#     test = json.loads(response.text)
#     print(test["prices"][0])
#     milliseconds = test["prices"][0]["time"][10:]
#     unixtime = test["prices"][0]["time"][0:10]
#     return test["prices"][0]
#
# def main():
#     usage = "usage: %prog [options]"
#     parser = OptionParser(usage)
#     parser.add_option("-b", "--displayHeartBeat", dest = "verbose", action = "store_true",
#                         help = "Display HeartBeat in streaming data")
#     displayHeartbeat = False
#
#     (options, args) = parser.parse_args()
#     if len(args) > 1:
#         parser.error("incorrect number of arguments")
#     if options.verbose:
#         displayHeartbeat = True
#     demo(displayHeartbeat)
#
#
# if __name__ == "__main__":
#     main()

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
        'Connection': 'keep-alive',
        # 'Accept-Encoding': 'gzip,deflate',
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
        # url = settings.STREAMING_DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/prices"
        # url = settings.STREAMING_DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/prices"
        params = {'instruments' : instruments}
        result = self.get(url, self.get_headers(None, True), params)
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    '''
    ticket
    '''
    def get_trades(self, accountModel, instruments, maxId = None, count=None):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/trades"
        params = {'instruments' : instruments}
        result = self.get(url, self._compressed_headers, params)
        if result.get_status():
            return result
        else:
            raise ZeroandaError(result)

    def close_trade(self, accountModel, trade_id):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/trades/" + trade_id
        # params = {'instruments' : instruments}
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
    def get_transactions(self, account_id, instrument, ids = None, count = None, max_id = None, min_id = None, etag = None):
        url = settings.DOMAIN + "/v1/accounts/" + str(account_id) + "/transactions"
        params = {}
        if ids != None:
            params["ids"] = ids
        else:
            params["instrument"] = instrument

            if count != None:
                params["count"] = count
            if max_id != None:
                params["maxId"] = max_id
            if min_id != None:
                params["minId"] = min_id
        if etag != None:
            utils.info("get_transactions: " + etag)
        else:
            utils.info("nothing")
        result = self.get(url, self.get_headers(etag), params)
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)
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
    def get_orders(self, account_id, instruments=None, maxId=None, count=None):
        url = settings.DOMAIN + "/v1/accounts/" + str(account_id) + "/orders"
        result = self.get(url, self._compressed_headers)

        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    def order_ifdoco(self, account_id, instruments, units, side, expiry, price, lowerBound, upperBound):
        payload = {'instrument': instruments,
                   'units': units,
                   'side': side,
                   'type': TYPE[2][0],
                   'expiry': timeutils.convert_rfc2unixtime(expiry),
                   'price': price,
                   'lowerBound': lowerBound,
                   'upperBound': upperBound,
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
        utils.info(result)
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result)

    # def delete(self, accountModel, trade_id):
    #     url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/trades/" + str(trade_id)
    #     result = self.delete(url, self._compressed_headers)
    #     utils.info(result)
    #     if result.get_status():
    #         return result
    #     else:
    #         utils.error(result.get_body())
    #         raise ZeroandaError(result)

    def events(self):
        url = settings.DOMAIN + "/v1/events/"

    def delete(self, url, headers, params = None):
        try:
            utils.info(headers)
            utils.info(url)
            utils.info(params)

            s = requests.Session()
            req = requests.Request('DELETE', url, headers=headers, params=params)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            return RequestDataObject(response)
            # return resp
        except Exception as e:
            s.close()

    def post(self, url, headers, payload):
        try:
            utils.info(headers)
            utils.info(url)
            utils.info(payload)
            s = requests.Session()
            req = requests.Request('POST', url, headers = headers, data = payload)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            return RequestDataObject(response)
        except Exception as e:
            s.close()

    def get(self, url, headers, params = None):
        try:
            s = requests.Session()
            utils.info(headers)
            utils.info(params)
            utils.info(url)
            req = requests.Request('GET', url, headers = headers, params = params)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            return RequestDataObject(response)
        except Exception as e:
            s.close()

    def options(self, url, headers, params = None):
        try:
            s = requests.Session()
            utils.info(headers)
            utils.info(url)
            req = requests.Request('OPTIONS', url, headers = headers, params = params)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            return RequestDataObject(response)
        except Exception as e:
            s.close()