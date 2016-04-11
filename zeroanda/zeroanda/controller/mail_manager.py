from django.core.mail import send_mail
from django.conf import settings

from zeroanda import utils
from zeroanda.classes.utils import timeutils

from datetime import datetime

class MailManager:
    @staticmethod
    def send_opening_mail(schedule):

        utils.info(timeutils.convert_datetime2str(timeutils.format_jst(schedule.presentation_time)))
        utils.info(timeutils.format_jst(schedule.presentation_time))

        # utils.info(d)
        subject =  "'" + schedule.title + "::" + timeutils.convert_datetime2str(timeutils.format_jst(schedule.presentation_time)) + "' begins. at " + timeutils.convert_datetime2str(datetime.now())
        message = "test"
        recipient_list = [settings.ADMIN_EMAIL]
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list= recipient_list
        )