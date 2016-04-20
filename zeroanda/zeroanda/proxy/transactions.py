from zeroanda.classes.utils import timeutils
from zeroanda.constant import TRANSACTION_TYPE, TRANSACTION_REASON
from zeroanda.models import TransactionModel
from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class TransactionsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_transactions(self, account_id, instrument, id = None, ids = None, count = None, etag = None):
        if etag == None:
            utils.info("none")

        response = self._streaming.get_transactions(account_id, instrument, id=id, ids=ids, count=count, etag=etag)
        utils.info("code: " + str(response.get_code()))
        # if response.get_status():
        return response
        # if response.get_code() == 200 or response.get_code() == 304 :
        #     return response
            # return response.get_body()

    def add(self, transaction, trade_id=0, schedule=None, actual_order_model=None):
        transaction_model = TransactionModel(
            trade_id=trade_id,
            schedule=schedule,
            actual_order_model=actual_order_model,
            instruments=transaction["instrument"],
            units=transaction["units"],
            side=transaction["side"],
            expiry=timeutils.convert_timestamp2datetime(transaction["expiry"]),
            price=transaction["price"],
            upperBound=transaction["upperBound"],
            lowerBound=transaction["lowerBound"],
            stopLoss=transaction["stopLossPrice"],
            type=self.transaction_type(transaction["type"]),
            reason=self.transaction_reason(transaction["reason"]),
            time=timeutils.convert_timestamp2datetime(transaction["time"]),
        )
        transaction_model.save()

    def transaction_type(self, value):
        for item in TRANSACTION_TYPE:
            if item[1] == value:
                return item[0]
        raise Exception('no constant for type.')

    def transaction_reason(self, value):
        for item in TRANSACTION_REASON:
            if item[1] == value:
                return item[0]
        raise Exception('no constant for reason.')