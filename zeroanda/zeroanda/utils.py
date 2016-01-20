from datetime import datetime, timezone, timedelta
import calendar, pytz, logging
logger =logging.getLogger("django")

def format_jst(date_time):
    JST = timezone(timedelta(hours=+9), 'JST')
    return datetime.fromtimestamp(date_time.timestamp(), JST)

def format_unixtime(time):
    milliseconds = time[10:]
    unixtime = time[0:10]
    return float(unixtime + "." + milliseconds)

def convert_rfc2unixtime(date_time):
    return calendar.timegm(date_time.astimezone(pytz.utc).timetuple())

def convert_timestamp2datetime(timestamp_data):
    return datetime.fromtimestamp(format_unixtime(timestamp_data))

def output(string):
    print(string)
    logger.info(string)