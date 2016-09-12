import calendar, pytz

from django.conf import settings

from zeroanda.classes.utils import timeutils
from zeroanda import utils

class EconomyIndicationValueObject:
    _raw_date   = None
    _raw_time   = None
    _time_zone  = None
    _currency   = None
    _event      = None
    _importance = None
    _actual     = 0
    _forecast   = 0
    _previous   = 0
    _date       = None

    def __init__(self, responce, target_date):
        if responce is None:
            return
        self._raw_date      = responce[0]
        self._raw_time      = responce[1]
        self._time_zone = responce[2]
        self._currency  = responce[3].upper()
        self._event     = responce[4]
        self._importance = responce[5].upper()
        self._actual    = responce[6]
        self._forecast  = responce[7]
        self._previous  = responce[8]

        if self._date != None and self._time != None:
            date_arr = self._date.split(" ")
            time_arr = self._time.split(":")
            if len(date_arr) == 3 and len(time_arr) == 2:
                year = target_date.year
                month = 1
                day = 1
                hour = 0
                second = 0

                day     = int(date_arr[2])
                hour    = int(time_arr[0])
                second  = int(time_arr[1])
                for i, v in enumerate(calendar.month_abbr):
                    if v == date_arr[1]:
                        month = i
                        break
                # utils.info(year)
                # utils.info(month)
                # utils.info(day)
                # utils.info(hour)
                # utils.info(second)
                d = timeutils.get_datetime(year=year, month=month, day=day, hour=hour, second=second, tzinfo=pytz.timezone(settings.STANDARD_TIME_ZONE))
                self._date = timeutils.convert_aware_datetime_from_utc_to_jst(d)
                # utils.info(d)
                # utils.info(d2)
                utils.info(self._date)


    def __str__(self):
        return self._event + ", " + self._raw_date + ", " + self._raw_time + ", " + self._time_zone + ", " + self._currency + ", " + self._importance