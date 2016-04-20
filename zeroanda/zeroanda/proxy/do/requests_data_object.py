import json
from zeroanda import utils

class RequestDataObject:
    _code    = None
    _headers = None
    _body = None
    def __init__(self, response):
        self._code = response.status_code
        self._headers    = response.headers
        self._body = None if response.status_code == 304 or response.status_code == 429 or response.text == None else response.text if response.headers["Content-Type"] != 'application/json' else json.loads(response.text)
    def get_code(self):
        return self._code

    def get_status(self):
        utils.info("status_code: " + str(self._code))
        return self._code == 200 or self._code == 304 or self._code == 201 or self._code == 429

    def get_etag(self):
        # for k, v in self._headers.items():
        #     utils.info(k)
        #     utils.info(v)
        result = self._headers["ETag"] if self._headers != None and "ETag" in self._headers else None
        return result

    def get_body(self):
        return self._body