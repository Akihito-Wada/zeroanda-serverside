from django.core.mail import send_mail
from django.conf import settings

from zeroanda import utils
from zeroanda.classes.utils import timeutils

from datetime import datetime

class MailManager:
    @staticmethod
    def send_opening_mail(schedule):
        subject =  "'" + schedule.title + "::" + timeutils.convert_datetime2str(timeutils.convert_aware_datetime_from_utc_to_jst(schedule.presentation_time)) + "' begins. at " + timeutils.convert_datetime2str(timeutils.get_now_with_jst())
        recipient_list = [settings.ADMIN_EMAIL]
        from_email = settings.DEFAULT_FROM_EMAIL
        message = "test"
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list= recipient_list
        )