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
    def writer(cls, dto):
        directory = dto.get_csv_path()
        os.makedirs(directory, exist_ok=True)

        target_file = os.path.join(directory, "{calendar_name}_{unique_id}.csv".format(calendar_name=cls.calendar_name, unique_id=dto.get_unique_id()))
        # if os.path.isfile(target_file):
        body = []
        for vo in dto.get_economic_indicator_list():
            if vo.date == None or vo.event == None: continue
            row = []
            row.append(vo.event)
            row.append(GoolgleCalendarCSV.format_date(vo.date))
            row.append(GoolgleCalendarCSV.format_time(vo.date))
            row.append(GoolgleCalendarCSV.format_date(vo.date))
            row.append(GoolgleCalendarCSV.format_time(vo.date))
            row.append("False")
            row.append(vo)
            row.append("")
            row.append("True")
            row.append(vo.currency)
            row.append(vo.get_importance())
            body.append(row)

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
