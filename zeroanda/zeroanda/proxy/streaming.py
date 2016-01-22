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

    def get_headers(self, model=None):
        if model == None or model.etag == None:
            return self._default_headers
        else:
            self._default_headers['If-None-Match'] = model.etag
            return self._default_headers
            # return self._default_headers.update({'If-None-Match': accountModel.etag})

    def accounts(self, accountModel = None):
        # if accountModel == None or accountModel.account_id == None:
        url = settings.DOMAIN + "/v1/accounts"
        # else:
        #     url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id)
        result = self.get(url, self.get_headers(accountModel))
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result.get_body())

    def account_info(self, accountModel, accountInfoModel = None):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id)
        result = self.get(url, self.get_headers(accountInfoModel))
        if result.get_status():
            return result
        else:
            utils.error(result.get_body())
            raise ZeroandaError(result.get_body())

    def get_orders(self, accountModel):
        if accountModel.account_id == None:
            raise Exception('account_id is None.')
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/orders"
        response = self.get(url, self._compressed_headers)

        if response.status_code != 200:
            error = json.loads(response.text)
            utils.error(error)
            raise ZeroandaError(error)
        else:
            return json.loads(response.text)

    def traders(self, accountModel, instruments, maxId = None, count=None):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/trades"
        params = {'instruments' : instruments}
        response = self.get(url, self._compressed_headers, params)
        if response.status_code != 200:
            error = json.loads(response.text)
            utils.error(error)
            raise ZeroandaError(error)
        else:
            return json.loads(response.text)

    def positions(self, accountModel):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/positions"
        # params = {'instruments' : instruments}
        response = self.get(url, self._compressed_headers)
        if response.status_code != 200:
            error = json.loads(response.text)
            utils.error(error)
            raise ZeroandaError(error)
        else:
            return json.loads(response.text)

    def prices(self, accountModel, instruments):
        url = settings.DOMAIN + "/v1/prices"
        # url = settings.STREAMING_DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/prices"
        # url = settings.STREAMING_DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/prices"
        params = {'instruments' : instruments}
        utils.info(self._compressed_headers)
        return
        response = self.get(url, self._default_headers, params)
        if response.status_code != 200:
            error = json.loads(response.text)
            utils.error(error)
            raise ZeroandaError(error)
        else:
            result = json.loads(response.text)
            print(result)
            return result["prices"][0]

    def order_ifdoco(self, accountModel, orderModel):

        payload = {'instrument': orderModel.instruments,
                   'units': orderModel.units,
                   'side': orderModel.side,
                   'type': orderModel.type,
                   'expiry': utils.convert_rfc2unixtime(orderModel.expiry),
                   'price': orderModel.price,
                   'lowerBound': orderModel.lowerBound,
                   'upperBound': orderModel.upperBound,
                   }

        if accountModel.account_id == None:
            raise Exception('account_id is None.')
        url = settings.STREAMING_DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/orders"
        response = self.post(url, self._compressed_headers, payload)

        if response.status_code != 201:
            error = json.loads(response.text)
            utils.error(error)
            raise ZeroandaError(error)
        else:
            return json.loads(response.text)

    def cancel_order(self, accountModel, actual_order_id):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/orders/" + str(actual_order_id)
        response = self.delete(url, self._compressed_headers)

        if response.status_code != 200:
            error = json.loads(response.text)
            raise ZeroandaError(error)
        else:
            result = json.loads(response.text)
            utils.info(result)

    def events(self):
        url = settings.DOMAIN + "/v1/events/"

    def delete(self, url, headers, params = None):
        try:
            s = requests.Session()
            req = requests.Request('DELETE', url, headers=headers, params=params)
            pre = req.prepare()
            resp = s.send(pre, stream = True, verify = False)
            return resp
        except Exception as e:
            s.close()

    def post(self, url, headers, payload):
        try:
            s = requests.Session()
            req = requests.Request('POST', url, headers = headers, data = payload)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            return response
        except Exception as e:
            s.close()

    def get(self, url, headers, params = None):
        try:
            s = requests.Session()
            utils.info(headers)
            utils.info(url)
            req = requests.Request('GET', url, headers = headers, params = params)
            pre = req.prepare()
            response = s.send(pre, stream = True, verify = False)
            # for k, v in response:
            #     utils.info(k + ", v: " + v)
            return RequestDataObject(response)
            # return response
        except Exception as e:
            s.close()