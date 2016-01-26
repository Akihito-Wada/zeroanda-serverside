from zeroanda.models import ErrorModel
class ZeroandaError(Exception):
    _status_code    = None
    _code   = None
    _message    = None
    info    = None
    def __init__(self, response):
        self._status_code   = response.get_code()
        self._code = response.get_body()["code"]
        self._message = response.get_body()["message"]
        self._info = response.get_body()["moreInfo"]

    def save(self):
        model = ErrorModel(code=self._code, message = self._message, info = self._info)
        model.save()

    def get_code(self):
        return self._code

    def get_status_code(self):
        return self._status_code