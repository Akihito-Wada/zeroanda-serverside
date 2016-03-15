from django import db
from django.conf import settings

from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.classes.utils import timeutils
from zeroanda.constant import INSTRUMENTS, EXPIRY_MINITES, IFDOCO_ENTRY_POINT
from zeroanda.proxy.order import OrderProxyModel
from zeroanda import utils

from datetime import datetime, timedelta

from multiprocessing import Process

import  pytz

class IfdococProcess(AbstractProcess):
    def __init__(self, task):
        self._jobs = []
        self.__orderProxyModel = OrderProxyModel()
        super(IfdococProcess, self).__init__(task)

    def _create_job(self):
        self._jobs.append(Process(target=self._order_buy))
        self._jobs.append(Process(target=self._order_sell))

    def _order_buy(self):
        db.close_old_connections()
        self.__orderProxyModel.buy_ifdoco(
                target_price=self._task.pool['price_model'].ask + IFDOCO_ENTRY_POINT,
                upper_bound=utils.get_ask_upper_bound(self._task.pool['price_model'].ask),
                lower_bound=utils.get_ask_lower_bound(self._task.pool['price_model'].ask),
                units= self._task.pool['ask_unit'],
                expiry= datetime.now(pytz.utc) + timedelta(minutes=EXPIRY_MINITES),
                accountId= self._task.pool['account_info_model'].account_id,
                instrument=INSTRUMENTS[0][0])

    def _order_sell(self):
        db.close_old_connections()
        self.__orderProxyModel.sell_ifdoco(
                target_price=self._task.pool['price_model'].bid - IFDOCO_ENTRY_POINT,
                upper_bound=utils.get_bid_upper_bound(self._task.pool['price_model'].bid),
                lower_bound=utils.get_bid_lower_bound(self._task.pool['price_model'].bid),
                units= self._task.pool['bid_unit'],
                expiry= datetime.now(pytz.utc) + timedelta(minutes=EXPIRY_MINITES),
                accountId= self._task.pool['account_info_model'].account_id,
                instrument=INSTRUMENTS[0][0])

    def _is_condition(self):
        if settings.TEST == True:
            return True
        return True

        now = timeutils.unixtime()
        presentation_time = int(timeutils.convert_rfc2unixtime(self._task.schedule.presentation_time))
        if presentation_time - now > 10:
            return False
        elif now > presentation_time:
            raise Exception('IfdococProcess::time is over.: ' + timeutils.format_date(now))
        return True