"""
Demonstrates streaming feature in OANDA open api

To execute, run the following command:

python streaming.py [options]

To show heartbeat, replace [options] by -b or --displayHeartBeat
"""

import requests
import json
import logging
import datetime
import time

logger =logging.getLogger("django")

from optparse import OptionParser
from settings import local_settings

def connect_to_stream(url):
    """

    Environment           <Domain>
    fxTrade               stream-fxtrade.oanda.com
    fxTrade Practice      stream-fxpractice.oanda.com
    sandbox               stream-sandbox.oanda.com
    """

    # Replace the following variables with your personal ones
    # domain = 'stream-fxpractice.oanda.com'
    # domain = 'api-sandbox.oanda.com'
    access_token = 'ACCESS-TOKEN'
    account_id = '1234567'
    # instruments = "EUR_USD,USD_CAD"

    try:
        s = requests.Session()
        # url = "https://" + domain + "/v1/prices"
        headers = {'Authorization' : 'Bearer ' + access_token,
                   # 'X-Accept-Datetime-Format' : 'unix'
                   'Content-type': 'application/x-www-form-urlencoded',
                   # 'X-Accept-Datetime-Format':'rfc3339',
                   'X-Accept-Datetime-Format':'unix',
                   'Connection': 'keep-alive',
                   'Accept-Encoding': 'gzip,deflate',
                  }
        # params = {'instruments' : instruments, 'accountId' : account_id}
        params = {'instruments' : ','.join(local_settings.INSTRUMENTS)}
        req = requests.Request('GET', url, headers = headers, params = params)
        pre = req.prepare()
        resp = s.send(pre, stream = True, verify = False)
        return resp
    except Exception as e:
        s.close()

        print("Caught exception when connecting to stream\n" + str(e))

def demo(displayHeartbeat):
    url = "http://" + local_settings.domain + "/v1/prices"
    response = connect_to_stream(url)
    if response.status_code != 200:
        print(response.text)
        return
    test = json.loads(response.text)
    # print(test["prices"][0]["instrument"])
    print(test["prices"])
    # print(datetime.datetime.fromtimestamp(int(test["prices"][0]["time"])))
    # for line in response.iter_lines(1):
    #     if line:
    #         try:
    #             print(line)
    #             msg = json.loads(line)
    #         except Exception as e:
    #             print("Caught exception when converting message into json\n" + str(e))
    #             return
    #
    #         if displayHeartbeat:
    #             print(line)
    #         else:
    #             if msg.has_key("instrument") or msg.has_key("tick"):
    #                 print(line)

def get_prices():
    print('get_prices')
    url = "http://" + local_settings.domain + "/v1/prices"
    response = connect_to_stream(url)
    if response.status_code != 200:
        print(response.text)
        return
    test = json.loads(response.text)
    print(test["prices"][0])
    # print(datetime.datetime.now())
    # print(test["prices"][0]["time"])
    milliseconds = test["prices"][0]["time"][10:]
    unixtime = test["prices"][0]["time"][0:10]
    # print(unixtime)
    # print(datetime.datetime.fromtimestamp(int(unixtime)).strftime('%Y-%m-%d %H:%M:%S') + "." + milliseconds)
    return test["prices"][0]

def main():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-b", "--displayHeartBeat", dest = "verbose", action = "store_true",
                        help = "Display HeartBeat in streaming data")
    displayHeartbeat = False

    (options, args) = parser.parse_args()
    if len(args) > 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        displayHeartbeat = True
    demo(displayHeartbeat)


if __name__ == "__main__":
    main()


class Streaming:
    access_token = 'ACCESS-TOKEN'
    account_id = '1234567'
    headers = {'Authorization' : 'Bearer ' + access_token,
               'Content-type': 'application/x-www-form-urlencoded',
               # 'X-Accept-Datetime-Format':'rfc3339',
               'X-Accept-Datetime-Format':'unix',
               'Connection': 'keep-alive',
               'Accept-Encoding': 'gzip,deflate',
              }

    @staticmethod
    def prices():
        url = "http://" + local_settings.domain + "/v1/prices"
        params = {'instruments' : ','.join(local_settings.INSTRUMENTS)}
        response = Streaming.get(url, params)
        if response.status_code != 200:
            print(response.text)
            return
        result = json.loads(response.text)
        return result["prices"][0]

    @staticmethod
    def order_ifdoco(side, price, lowerBound, upperBound):
        print('order_ifdoco')
        payload = {'instrument': 'EUR_USD',
                   'units': 2,
                   'side': side,
                   'type': 'marketIfTouched',
                   'expiry': '',
                   'price': price,
                   'lowerBound': lowerBound,
                   'upperBound': upperBound,
                   }
        url = "http://" + local_settings.domain + "/v1/accounts/12345/orders"
        response = Streaming.post(url, payload)
        if response.status_code != 200:
            print(response.text)
            return
        result = json.loads(response.text)
        print(result)

    @staticmethod
    def orders():
        print('orders')
        payload = {'instrument': 'EUR_USD',
                   'units': 2,
                   'side': 'sell',
                   'type': 'marketIfTouched',
                   'expiry': '',
                   'price': '',
                   'lowerBound': '',
                   'upperBound': ''
                   }
        url = "http://" + local_settings.domain + "/v1/accounts/12345/orders"
        response = Streaming.post(url, payload)
        if response.status_code != 200:
            print(response.text)
            return
        result = json.loads(response.text)
        print(result)

    @staticmethod
    def post(url, payload):
        try:
            s = requests.Session()
            headers = Streaming.headers
            req = requests.post(url=url, data=payload)
            return req
            # req = requests.Request('POST', url, headers = headers, params = payload)
            # pre = req.prepare()
            # resp = s.send(pre, stream = True, verify = False)
            # return resp
        except Exception as e:
            s.close()

    @staticmethod
    def get(url, params):
        try:
            s = requests.Session()
            req = requests.Request('GET', url, headers = Streaming.headers, params = params)
            pre = req.prepare()
            resp = s.send(pre, stream = True, verify = False)
            return resp
        except Exception as e:
            s.close()