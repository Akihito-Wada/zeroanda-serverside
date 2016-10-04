import csv, os
from datetime   import datetime

from zeroanda import utils

class CSVFactory:
    @staticmethod
    def create():
        return GoolgleCalendarCSV()

class CSV(object):
    @classmethod
    def reader(cls, content):
        decoded_content = content.decode('utf-8')
        return csv.reader(decoded_content.splitlines(), delimiter=',')

class GoolgleCalendarCSV(CSV):
    calendar_name   = "economic_indicator_calendar"
    header          = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event', 'Description', 'Location', 'Private', 'Currency', 'Importance']

    @classmethod
    def writer(cls, path, body, suffix = None):
        os.makedirs(path, exist_ok=True)
        if suffix != None:
            target_file = os.path.join(path, "{calendar_name}_{suffix}.csv".format(calendar_name=cls.calendar_name, suffix=suffix))
        else:
            target_file = os.path.join(path, "{calendar_name}.csv".format(calendar_name=cls.calendar_name))

        with open(target_file, 'w') as f:
            writer = csv.writer(f)  # writerオブジェクトを作成
            writer.writerow(cls.header)  # ヘッダーを書き込む
            writer.writerows(body)  # 内容を書き込む

    @staticmethod
    def format_date(date):
        formatted_date = date.strftime("%m/%d/%Y")
        return formatted_date

    @staticmethod
    def format_time(date):
        formatted_time = date.strftime("%I:%M %p")
        return formatted_time
