from zeroanda.models import ErrorModel
class ZeroandaError(Exception):
    _code   = None
    _message    = None
    info    = None
    def __init__(self, error):
        self._code = error["code"]
        self._message = error["message"]
        self._info = error["moreInfo"]

    def save(self):
        print('save')
        model = ErrorModel(code=self._code, message = self._message, info = self._info)
        model.save()