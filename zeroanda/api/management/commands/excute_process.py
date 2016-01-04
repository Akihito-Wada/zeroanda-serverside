from django.core.management.base import BaseCommand, CommandError
from zeroanda import  streaming
from settings import local_settings
import time
import logging

logger =logging.getLogger("django")

class Command(BaseCommand):
    help = 'excute process.'
    def handle(self, *args, **options):
        # streaming.demo(True)
        i = 0
        while i < 3:
            streaming.get_prices()
            time.sleep(local_settings.WAIT_TIME)
            i += 1