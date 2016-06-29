from django.core.mail import send_mail
from django.conf import settings

from zeroanda import utils
from zeroanda.classes.utils import timeutils

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

    @staticmethod
    def send_finish_mail(schedule):
        subject = "'" + schedule.title + "::" + timeutils.convert_datetime2str(
            timeutils.convert_aware_datetime_from_utc_to_jst(
                schedule.presentation_time)) + "' finish. at " + timeutils.convert_datetime2str(
            timeutils.get_now_with_jst())
        recipient_list = [settings.ADMIN_EMAIL]
        from_email = settings.DEFAULT_FROM_EMAIL
        message = "finish"
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list
        )

    @staticmethod
    def send_mail_test():
        import smtplib

        # Import the email modules we'll need
        from email.mime.text import MIMEText

        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        # with open(textfile) as fp:
            # Create a text/plain message
        msg = 'test'

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'The contents of %s'
        msg['From'] = 'system@zeroanda.com'
        msg['To'] = '13southdawn10@gmail.com'

        # Send the message via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()