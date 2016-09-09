from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class CalenderProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_calenders(self, instrument, period):
        try:
            calender_list = []
            response = self._streaming.calender(instrument, period)
            if response.get_code() == 200:
                calenders = response.get_body()
                utils.info(isinstance(calenders, list))
                utils.info(type(calenders))
                for calender in calenders:
                    utils.info(calender)
                    vo = CalenderValueObject(calender)
                    calender_list.append(vo)
                return calender_list
                # return sorted(calender_list, key=attrgetter('id'), reverse=True)
            else:
                return None
        except:
            return None

class CalenderValueObject:
    def __init__(self):return