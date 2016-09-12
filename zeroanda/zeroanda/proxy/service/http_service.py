from  zeroanda.classes.net.http import Http
import calendar
import csv
from datetime   import datetime
from dateutil.relativedelta import relativedelta
from zeroanda import utils
from zeroanda.proxy.do.economy_indication_value_object import EconomyIndicationValueObject

class HttpService:
    url = ""

    @classmethod
    def create(cls):
        return DailyFXService()

    def get_economic_indicator(self, url):
        if url is None:
            raise Exception('not define url.')
        http = Http()
        return http.get_csv_file(url)

class DailyFXService(HttpService):
    url = "http://www.dailyfx.com"

    def get_latest_economic_indicator(self):
        target_url = self.url + "/files/Calendar-09-11-2016.csv"
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day

        # target_date = self.get_next_sunday_datetime(year, 12, 26)
        target_date = self.get_next_sunday_datetime(year, month, day)
        # target_url = self.url + "/files/Calendar-" + str("{0:02d}".format(target_date.month)) + "-" + str("{0:02d}".format(target_date.day)) + "-" + str(target_date.year) + ".csv"
        utils.info(target_url)
        result = self.get_economic_indicator(target_url)

        decoded_content = result.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        _tmp_list = list(cr)
        _list = []
        for index, row in enumerate(_tmp_list):
            if index == 0:
                continue
            vo = EconomyIndicationValueObject(row, target_date)
            utils.info(vo)
            _list.append(vo)
        return _list

    def get_next_sunday_datetime(self, year, month, day):
        origin_date = datetime(year=year, month=month, day=day)
        utils.info(origin_date)
        for x in calendar.monthcalendar(year, month):
            if x[calendar.SUNDAY] <= 0:
                break
            next_sunday_candidate = datetime(year=year, month=month, day=x[calendar.SUNDAY])
            if next_sunday_candidate >= origin_date:
                return next_sunday_candidate
        next_month = origin_date + relativedelta(months=1)
        return self.get_next_sunday_datetime(next_month.year, next_month.month, 1)
