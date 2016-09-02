import logging
import math

from django.conf import settings

logger =logging.getLogger("django")

def info(value):
    logger.info(value)

def error(value):
    logger.error(value)

def get_max_units(balance, rate):
    units = balance * settings.LEVERAGE / rate / settings.CURRENCY * 1000;
    return int(math.floor(units))

def get_ask_target_point(reference_value):
    return math.floor((reference_value + settings.IFDOCO_ASK_ENTRY_POINT) * 1000) / 1000

def get_ask_upper_bound(reference_value):
    target = math.floor((reference_value + settings.ASK_UPPER_BOUND_PROFIT_MARGIN) * 1000) / 1000
    return target

def get_ask_lower_bound(reference_value):
    target = math.floor((reference_value + settings.ASK_LOWER_BOUND_PROFIT_MARGIN) * 1000) / 1000
    return target

def get_ask_stop_loss(reference_value):
    target = math.floor((reference_value + settings.ASK_STOP_LOSS_MARGIN) * 1000) / 1000
    return target

def get_bid_target_point(reference_value):
    target = math.floor((reference_value + settings.IFDOCO_BID_ENTRY_POINT) * 1000) / 1000
    return target

def get_bid_upper_bound(reference_value):
    target = math.floor((reference_value + settings.BID_UPPER_BOUND_PROFIT_MARGIN) * 1000) / 1000
    return target

def get_bid_lower_bound(reference_value):
    target = math.floor((reference_value + settings.BID_LOWER_BOUND_PROFIT_MARGIN) * 1000) / 1000
    return target

def get_bid_stop_loss(reference_value):
    target = math.floor((reference_value + settings.BID_STOP_LOSS_MARGIN) * 1000) / 1000
    return target
