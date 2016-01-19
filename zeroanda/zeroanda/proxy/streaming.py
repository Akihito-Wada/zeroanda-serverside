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
    # access_token = 'ACCESS-TOKEN'
    account_id = '1234567'
    # instruments = "EUR_USD,USD_CAD"

    try:
        s = requests.Session()
        # url = "https://" + domain + "/v1/prices"
        headers = {'Authorization' : 'Bearer ' + settings.TOKEN,
                   'Content-type': 'application/x-www-form-urlencoded',
                   'X-Accept-Datetime-Format':'unix',
                   'Connection': 'keep-alive',
                   'Accept-Encoding': 'gzip,deflate',
                  }
        # params = {'instruments' : instruments, 'accountId' : account_id}
        params = {'instruments' : ','.join(settings.INSTRUMENTS)}
        req = requests.Request('GET', url, headers = headers, params = params)
        pre = req.prepare()
        resp = s.send(pre, stream = True, verify = False)
        return resp
    except Exception as e:
        s.close()

        print("Caught exception when connecting to stream\n" + str(e))

def demo(displayHeartbeat):
    url = "http://" + settings.DOMAIN + "/v1/prices"
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
    url = settings.DOMAIN + "/v1/prices"
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

from zeroanda.errors import ZeroandaError
import logging, calendar, pytz

class Streaming(object):
    # _account_id = None
    _default_headers = {
        'Authorization' : 'Bearer ' + settings.TOKEN,
        'Content-type': 'application/x-www-form-urlencoded',
        'X-Accept-Datetime-Format':'unix',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip,deflate',
    }

    def accounts(self, accountId = None):
        if accountId == None:
            url = settings.DOMAIN + "/v1/accounts"
        else:
            url = settings.DOMAIN + "/v1/accounts/" + str(accountId)
        response = self.get(url, self._default_headers)
        if response.status_code != 200:
            error = json.loads(response.text)
            print(error)
            raise ZeroandaError(error)
        result = json.loads(response.text)
        return result

    def traders(self, accountModel, instruments, maxId = None, count=None):
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/trades"
        params = {'instruments' : instruments}
        response = self.get(url, self._default_headers, params)
        if response.status_code != 200:
            error = json.loads(response.text)
            print(error)
            raise ZeroandaError(error)
        else:
            result = json.loads(response.text)
            print(result)

    def prices(self, instruments):
        url = settings.DOMAIN + "/v1/prices"
        params = {'instruments' : instruments}
        response = self.get(url, self._default_headers, params)
        if response.status_code != 200:
            error = json.loads(response.text)
            print(error)
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
                   # 'expiry': orderModel.expirey,
                   'expiry': calendar.timegm(orderModel.expirey.astimezone(pytz.utc).timetuple()),
                   'price': orderModel.price,
                   'lowerBound': orderModel.lowerBound,
                   'upperBound': orderModel.upperBound,
                   }

        if accountModel.account_id == None:
            raise Exception('account_id is None.')
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/orders"
        response = self.post(url, self._default_headers, payload)

        if response.status_code != 201:
            error = json.loads(response.text)
            print(error)
            logger.info(error)
            raise ZeroandaError(error)
        else:
            result = json.loads(response.text)
            print(result)
            logger.info(result)
            return result

    def get_orders(self, accountModel):
        if accountModel.account_id == None:
            raise Exception('account_id is None.')
        url = settings.DOMAIN + "/v1/accounts/" + str(accountModel.account_id) + "/orders"
        response = self.get(url, self._default_headers)

        if response.status_code != 200:
            error = json.loads(response.text)
            print(error)
            raise ZeroandaError(error)
        else:
            result = json.loads(response.text)
            print(result)
            logger.info(result)

    def events(self):
        url = settings.DOMAIN + "/v1/events/"

    def post(self, url, headers, payload):
        try:
            s = requests.Session()
            # headers = {
            #     'Authorization' : 'Bearer ' + '8713400a434b3f4cfd2e2f9580da45ed-41a3452617aa84f441be90ca6ab0fc55',
            #
            #     'Content-type': 'application/x-www-form-urlencoded',
            #     # 'X-Accept-Datetime-Format':'RFC3339',
            #     'X-Accept-Datetime-Format':'unix',
            #     'Connection': 'keep-alive',
            #     'Accept-Encoding': 'gzip,deflate',
            # }
            req = requests.post(url=url, headers = headers, data=payload)
            # req = requests.post(url=url, headers = headers, payload=payload)
            logger.info(req)

# curl -X POST -H "Authorization: Bearer 8713400a434b3f4cfd2e2f9580da45ed-41a3452617aa84f441be90ca6ab0fc55" -d "instrument=EUR_USD&units=2&side=sell&type=marketIfTouched&price=1.2&expiry=2016-04-01T00%3A00%3A00Z" "https://api-fxpractice.oanda.com/v1/accounts/6818465/orders"
            return req

            # req = requests.Request('POST', url, headers = headers, params = payload)
            # pre = req.prepare()
            # resp = s.send(pre, stream = True, verify = False)
            # return resp
        except Exception as e:
            s.close()

    def get(self, url, headers, params = None):
        try:
            print(url)
            print(headers)
            print(params)
            logger.info(url)
            logger.info(headers)
            logger.info(params)
            s = requests.Session()
            req = requests.Request('GET', url, headers = headers, params = params)
            pre = req.prepare()
            resp = s.send(pre, stream = True, verify = False)
            return resp
        except Exception as e:
            s.close()