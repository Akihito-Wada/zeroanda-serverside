import calendar, csv, os
from datetime   import datetime
from dateutil.relativedelta import relativedelta
from django.conf    import settings

from zeroanda import utils
from zeroanda.classes.net.http import Http
from zeroanda.classes.utils.csv_utils import CSVFactory
from zeroanda.services.economic_indicator.vo.economy_indication_value_object import EconomyIndicationValueObject


class EconomicIndicatorApiServiceFactory:
    @classmethod
    def create(cls):
        return DailyFXService()

class HttpService:
    _url = ""

    def get_economic_indicator(self, url):
        if url is None:
            raise Exception('not define url.')
        http = Http()
        return http.get_csv_file(url)

class DailyFXService(HttpService):
    _service_name = "dailyfx.com"
    _url = "http://www.dailyfx.com"

    def get_latest_economic_indicator(self):
        year = datetime.now().year
        month = datetime.now().month
        # day = datetime.now().day
        day = 11

        target_date = self.__get_next_sunday_datetime(year, month, day)
        unique_id   = "{month}-{day}-{year}".format(month=str("{0:02d}".format(target_date.month)), day=str("{0:02d}".format(target_date.day)), year=str(target_date.year))
        filename    = "Calendar-{unique_id}.csv".format(unique_id=unique_id)
        target_url  = "{url}/files/{filename}".format(url=self._url, filename=filename)
        result      = self.get_economic_indicator(target_url)
        _tmp_list   = CSVFactory.create().reader(result.content)
        _list = []
        for index, row in enumerate(_tmp_list):
            if index == 0:
                continue
            vo = EconomyIndicationValueObject(row, target_date)
            # utils.info(vo)
            _list.append(vo)
        dto = EconomicIndicatorDTO(self._service_name, unique_id, target_url, filename, _list, year, month, day)
        return dto

    def __get_next_sunday_datetime(self, year, month, day):
        origin_date = datetime(year=year, month=month, day=day)
        utils.info(origin_date)
        for x in calendar.monthcalendar(year, month):
            if x[calendar.SUNDAY] <= 0:
                break
            next_sunday_candidate = datetime(year=year, month=month, day=x[calendar.SUNDAY])
            if next_sunday_candidate >= origin_date:
                return next_sunday_candidate
        next_month = origin_date + relativedelta(months=1)
        return self.__get_next_sunday_datetime(next_month.year, next_month.month, 1)

class EconomicIndicatorDTO:
    _origin     = None
    _unique_id  = None
    _url        = None
    _filename   = None
    _list       = None
    _year       = 0
    _month      = 0
    _day        = 0
    def __init__(self, origin, unique_id, url, filename, list, year, month, day):
        self._origin    = origin
        self._unique_id = unique_id
        self._url       = url
        self._filename  = filename
        self._list      = list
        self._year      = year
        self._month     = month
        self._day       = day

    def get_origin(self):
        return self._origin

    def get_unique_id(self):
        return self._unique_id

    def get_url(self):
        return self._url

    def get_filename(self):
        return self._filename

    def get_economic_indicator_list(self):
        return self._list

    def get_csv_path(self):
        return os.path.join(settings.ECONOMIC_INDICATOR_CSV_FILES, str(self._year), str("{0:02d}".format(self._month)))

    def __str__(self):
        return "{origin}: {unique_id}".format(origin=self._origin, unique_id=self._unique_id)