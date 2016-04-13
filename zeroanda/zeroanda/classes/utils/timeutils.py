from datetime import datetime, timezone, timedelta
import calendar, pytz, logging, time
from zeroanda.utils import utils
from django.conf import settings

logger =logging.getLogger("django")

'''
メソッドにアクセスした時刻のUnixtimeを返す(int)
'''
def unixtime():
    return calendar.timegm(datetime.utcnow().timetuple())

def format_date(time_int):
    return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time_int))

'''
tzinfoがUTCな現在時間のAwareなDatetimeを返す
'''
def get_now_with_utc():
    return datetime.now(pytz.utc)

'''
tzinfoがJST(Asia/Tokyo)な現在時間のAwareなDatetimeを返す
'''
def get_now_with_jst():
    return datetime.now(pytz.timezone(settings.TIME_ZONE))

'''
AwareなDatetime（UTC）情報をJSTに変換する
'''
def convert_aware_datetime_from_utc_to_jst(date_time):
    JST = timezone(timedelta(hours=+9), 'JST')
    return datetime.fromtimestamp(date_time.timestamp(), JST)

def format_unixtime_to_jst(unixtime):
    JST = timezone(timedelta(hours=+9), 'JST')
    return datetime.fromtimestamp(int(unixtime), JST)

def format_unixtime(time):
    milliseconds = time[10:]
    unixtime = time[0:10]
    return float(unixtime + "." + milliseconds)

def convert_rfc2unixtime(date_time):
    return calendar.timegm(date_time.astimezone(pytz.utc).timetuple())

def convert_naive_rfc2unixtime(date_time):
    return date_time.strftime('%s')

def convert_timestamp2datetime(timestamp_data):
    return datetime.fromtimestamp(format_unixtime(timestamp_data))

def convert_datetime2str(date_time):
    return date_time.strftime("%Y/%m/%d %H:%M:%S")

'''
入力した年月日からDateTimeを返す
'''
def get_datetime(year, month, day, hour=0, minute=0, second=0, tzinfo=pytz.timezone(settings.TIME_ZONE)):
    return datetime(year, month, day, hour=hour, minute=minute, second=second, tzinfo=tzinfo)

'''
入力した年月日からunixtimeを返す
'''
def get_unixtime(year, month, day, hour=0, minute=0, second=0, tzinfo=pytz.timezone(settings.TIME_ZONE)):
    return int(calendar.timegm(get_datetime(year, month, day, hour, minute, second, tzinfo).timetuple()))
