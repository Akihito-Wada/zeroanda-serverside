from datetime import datetime, timezone, timedelta
import calendar, pytz, logging, time
from zeroanda.utils import utils

logger =logging.getLogger("django")

def unixtime():
    return int(time.time())

def format_date(time_int):
    return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time_int))

def format_jst(date_time):
    JST = timezone(timedelta(hours=+9), 'JST')
    return datetime.fromtimestamp(date_time.timestamp(), JST)

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

def convert_datetime2str(datetime):
    return datetime.strftime("%Y/%m/%d %H:%M:%S")

def get_datetime(year, month, day, hour, minute, second):
    return int(datetime(year, month, day, hour=hour, minute=minute, second=second).timestamp())
