from zeroanda import utils

import math

class PointMapProxy:

    def __init__(self, reference_value, priority):
        self._reference_value = reference_value
        self._priority = priority

class AskPointMapProxy(PointMapProxy):
    def __init__(self, reference_value, priority):
        super(AskPointMapProxy, self).__init__(reference_value, priority)

    def get_target_point(self):
        return math.floor((self._reference_value + POINT_MAP[self._priority]["IFDOCO_ASK_ENTRY_POINT"]) * 1000) / 1000

    def get_upper_bound(self):
        target = math.floor((self.get_target_point() + POINT_MAP[self._priority]["ASK_UPPER_BOUND_PROFIT_MARGIN"]) * 1000) / 1000
        return target

    def get_lower_bound(self):
        target = math.floor((self.get_target_point() + POINT_MAP[self._priority]["ASK_LOWER_BOUND_PROFIT_MARGIN"]) * 1000) / 1000
        return target

    def get_stop_loss(self):
        target = math.floor((self.get_target_point() + POINT_MAP[self._priority]["ASK_STOP_LOSS_MARGIN"]) * 1000) / 1000
        return target

class BidPointMapProxy(PointMapProxy):
    def __init__(self, reference_value, priority):
        super(BidPointMapProxy, self).__init__(reference_value, priority)
        
    def get_target_point(self):
        return math.floor((self._reference_value + POINT_MAP[self._priority]["IFDOCO_BID_ENTRY_POINT"]) * 1000) / 1000

    def get_upper_bound(self):
        target = math.floor((self.get_target_point() + POINT_MAP[self._priority]["BID_UPPER_BOUND_PROFIT_MARGIN"]) * 1000) / 1000
        return target

    def get_lower_bound(self):
        target = math.floor((self.get_target_point() + POINT_MAP[self._priority]["BID_LOWER_BOUND_PROFIT_MARGIN"]) * 1000) / 1000
        return target

    def get_stop_loss(self):
        target = math.floor((self.get_target_point() + POINT_MAP[self._priority]["BID_STOP_LOSS_MARGIN"]) * 1000) / 1000
        return target

POINT_MAP = (
    {
        "IFDOCO_ASK_ENTRY_POINT": 0.01,
        "ASK_UPPER_BOUND_PROFIT_MARGIN": 0.02,
        "ASK_LOWER_BOUND_PROFIT_MARGIN": -0.01,
        "ASK_STOP_LOSS_MARGIN": -0.02,

        "IFDOCO_BID_ENTRY_POINT": -0.01,
        "BID_UPPER_BOUND_PROFIT_MARGIN": 0.01,
        "BID_LOWER_BOUND_PROFIT_MARGIN": -0.02,
        "BID_STOP_LOSS_MARGIN": 0.02,
    },
    {
        "IFDOCO_ASK_ENTRY_POINT": 0.02,
        "ASK_UPPER_BOUND_PROFIT_MARGIN": 0.03,
        "ASK_LOWER_BOUND_PROFIT_MARGIN": -0.02,
        "ASK_STOP_LOSS_MARGIN": -0.03,

        "IFDOCO_BID_ENTRY_POINT": -0.02,
        "BID_UPPER_BOUND_PROFIT_MARGIN": 0.02,
        "BID_LOWER_BOUND_PROFIT_MARGIN": -0.03,
        "BID_STOP_LOSS_MARGIN": 0.03,
    },
    {
        "IFDOCO_ASK_ENTRY_POINT": 0.05,
        "ASK_UPPER_BOUND_PROFIT_MARGIN": 0.1,
        "ASK_LOWER_BOUND_PROFIT_MARGIN": -0.05,
        "ASK_STOP_LOSS_MARGIN": -0.1,

        "IFDOCO_BID_ENTRY_POINT": -0.05,
        "BID_UPPER_BOUND_PROFIT_MARGIN": 0.05,
        "BID_LOWER_BOUND_PROFIT_MARGIN": -0.1,
        "BID_STOP_LOSS_MARGIN": 0.1,
    },
)