import ast
import json
from zeroanda import utils

class RequestDataObject:
    _response = None
    _code    = None
    _headers = None
    _body = None
    def __init__(self, response):
        self._response = response
        self._code = response.status_code
        self._headers    = response.headers
        self._body = None if response.status_code == 304 or response.status_code == 429 or not response.text else response.text if response.headers["Content-Type"] != 'application/json' else json.loads(response.text)
    def get_code(self):
        return self._code

    def get_status(self):
        utils.info("status_code: " + str(self._code))
        return self._code == 200 or self._code == 304 or self._code == 201 or self._code == 429

    def get_etag(self):
        result = self._headers["ETag"] if self._headers != None and "ETag" in self._headers else None
        return result

    def get_body(self):
        return self._body

    def __str__(self):
        ret = "RequestDataObject."
        if self._response == None:
            ret += ".response is None."
            return self._response
        if self._code != None:
            ret += "\n  code: " + str(self._code)
        if self._headers != None:
            ret += "\n  headers: " + str(self._headers)
        if self._body != None:
            ret += "\n  body: " + str(self._body)
        return ret