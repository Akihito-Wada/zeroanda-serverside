from zeroanda.classes.task.children.aprocess import AbstractProcess
from zeroanda.constant import INSTRUMENTS
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
        # self._jobs.append(Process(target=self._order_sell()))

    def _order_buy(self):
        # expiry = datetime.now(pytz.utc) + timedelta(minutes=1)
        # utils.info(expiry)
        # utils.convert_rfc2unixtime(expiry)
        self.__orderProxyModel.buy_ifdoco(
                target_price=self._task.pool['price_model'].ask + 100,
                upper_bound=utils.get_ask_upper_bound(self._task.pool['price_model'].ask),
                lower_bound=utils.get_ask_lower_bound(self._task.pool['price_model'].ask),
                units= self._task.pool['ask_unit'],
                expiry= datetime.now(pytz.utc) + timedelta(minutes=1),
                accountId= self._task.pool['account_info_model'].account_id,
                instrument=INSTRUMENTS[0][0])

    def _is_condition(self):
        return True