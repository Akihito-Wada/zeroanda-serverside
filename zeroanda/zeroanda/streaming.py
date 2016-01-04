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

def connect_to_stream():
    """

    Environment           <Domain>
    fxTrade               stream-fxtrade.oanda.com
    fxTrade Practice      stream-fxpractice.oanda.com
    sandbox               stream-sandbox.oanda.com
    """

    # Replace the following variables with your personal ones
    # domain = 'stream-fxpractice.oanda.com'
    domain = 'api-sandbox.oanda.com'
    access_token = 'ACCESS-TOKEN'
    account_id = '1234567'
    instruments = "EUR_USD,USD_CAD"

    try:
        s = requests.Session()
        # url = "https://" + domain + "/v1/prices"
        url = "http://" + domain + "/v1/prices"
        headers = {'Authorization' : 'Bearer ' + access_token,
                   # 'X-Accept-Datetime-Format' : 'unix'
                   'Content-type': 'application/x-www-form-urlencoded',
                   'X-Accept-Datetime-Format':'UNIX',
                  }
        # params = {'instruments' : instruments, 'accountId' : account_id}
        params = {'instruments' : instruments}
        req = requests.Request('GET', url, headers = headers, params = params)
        pre = req.prepare()
        resp = s.send(pre, stream = True, verify = False)
        return resp
    except Exception as e:
        s.close()

        logger.info("Caught exception when connecting to stream\n" + str(e))

def demo(displayHeartbeat):
    response = connect_to_stream()
    if response.status_code != 200:
        logger.error(response.text)
        return
    print(response.text)
    test = json.loads(response.text)
    print(len(test["prices"]))
    # print(test["prices"][0]["instrument"])
    print(test["prices"])
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


