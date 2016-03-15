import logging
import math

from zeroanda import utils

from django.conf import settings

logger =logging.getLogger("django")

def info(value):
    # if isinstance(value, dict):
    #     value = json.loads(value)
    logger.info(value)
    # print(value)

def error(value):
    # if isinstance(value, dict):
    #     value = json.loads(value)
    logger.error(value)
    # print("error: " + value)

def get_max_units(balance, rate):
    units = balance * settings.LEVERAGE / rate / settings.CURRENCY;
    return int(math.floor(units))

def get_ask_upper_bound(reference_value):
    return math.floor((reference_value + 0.1) * 1000) / 1000

def get_ask_lower_bound(reference_value):
    return math.floor((reference_value - 0.1) * 1000) / 1000

def get_bid_upper_bound(reference_value):
    return math.floor((reference_value + 0.1) * 1000) / 1000

def get_bid_lower_bound(reference_value):
    return math.floor((reference_value - 0.1) * 1000) / 1000