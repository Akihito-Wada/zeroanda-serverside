import calendar, pytz

from django.conf import settings

from zeroanda.classes.utils import timeutils
from zeroanda.constant import ECONOMIC_INDICATOR_IMPORTANCE
from zeroanda import utils

class EconomyIndicationValueObject:
    raw_date   = None
    raw_time   = None
    time_zone  = None
    currency   = None
    event      = None
    importance = 0
    actual     = None
    forecast   = None
    previous   = None
    date       = None
    description = None

    def __init__(self, responce, target_date):
        if responce is None:
            return
        self.raw_date      = responce[0]
        self.raw_time      = responce[1]
        self.time_zone = responce[2]
        self.currency  = responce[3].upper()
        self.event     = responce[4]
        self.importance = self.__importance_type_key(responce[5].upper())
        self.actual    = responce[6]
        self.forecast  = responce[7]
        self.previous  = responce[8]
        if self.raw_date != None and self.raw_time != None:
            date_arr = self.raw_date.split(" ")
            time_arr = self.raw_time.split(":")
            if len(date_arr) == 3 and len(time_arr) == 2:
                year = target_date.year
                month = 1
                day = 1
                hour = 0
                second = 0

                day     = int(date_arr[2])
                hour    = int(time_arr[0])
                minute  = int(time_arr[1])
                for i, v in enumerate(calendar.month_abbr):
                    if v == date_arr[1]:
                        month = i
                        break
                d = timeutils.get_datetime(year=year, month=month, day=day, hour=hour, minute=minute, tzinfo=pytz.timezone(settings.STANDARD_TIME_ZONE))
                self.date = timeutils.convert_aware_datetime_from_utc_to_jst(d)

        self.description = "event: {event}, currency: {currency}, date={date} {timezone}, importance={importance}, actual={actual}, previous={previous}, forecast={forcast}".format(
            event=self.event, currency=self.currency, date=self.date, timezone=self.time_zone,
            importance=self.__importance_type_value(self.importance), actual=self.actual,
            previous=self.previous, forcast=self.forecast)

    def get_importance(self):
        return self.__importance_type_value(self.importance)

    def __importance_type_key(self, value):

        for item in ECONOMIC_INDICATOR_IMPORTANCE:
            if item[1] == value:
                return item[0]
        raise Exception('no constant for type.')

    def __importance_type_value(self, value):

        for item in ECONOMIC_INDICATOR_IMPORTANCE:
            if item[0] == value:
                return item[1]
        raise Exception('no constant for type.')

    def __str__(self):
        return self.description