class Etag(object):
    __instance = None
    _dic    = {}

    def __new__(cls, *args, **keys):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def get(self, model):
        if self._dic.has_key(model):
            return self._dic[model]
        else:
            return None

