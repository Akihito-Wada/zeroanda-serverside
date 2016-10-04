from django.core.management.base import BaseCommand, CommandError
from zeroanda.controller.action import Action
import logging

logger =logging.getLogger("django")

class Command(BaseCommand):
    help = 'get economic-indicator process.'
    def handle(self, *args, **options):
        action = Action()
        action.WatchEconomicIndicator()
