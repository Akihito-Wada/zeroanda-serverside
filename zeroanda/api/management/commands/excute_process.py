from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
import time

import logging

logger =logging.getLogger("django")

class Command(BaseCommand):
    help = 'excute process.'
    def handle(self, *args, **options):
        logger.info('test')