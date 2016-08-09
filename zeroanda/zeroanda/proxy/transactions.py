from zeroanda.classes.utils import timeutils
from zeroanda.constant import TRANSACTION_TYPE, TRANSACTION_REASON
from zeroanda.models import TransactionModel
from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class TransactionsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_transactions(self, account_id=None, instrument=None, id = None, ids = None, count = None, etag = None, actual_order_model_id=None):
        if actual_order_model_id != None:
            return TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id)
        else:
            response = self._streaming.get_transactions(account_id, instrument, id=id, ids=ids, count=count, etag=etag)
            return response

    def get_latest_transaction_by_id(self, actual_order_model_id):
        try:
            return TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id).order_by('-id')[:1][0]
        except:
            return None

    def get_latest_type(self, actual_order_model_id):
        try:
            model = TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id).order_by('-id')[:1][0]
            return self.transaction_type_value(model.type)
        except:
            return None

    def get_latest_transaction_reason_value(self, actual_order_model_id):
        try:
            model = TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id).order_by('-id')[:1][0]
            return self.transaction_reason_value(model.reason)
        except:
            return None

    def add(self, transaction, trade_id=0, schedule=None, actual_order_model=None):
        transaction_model = TransactionModel(
            actual_order_id=transaction["id"],
            trade_id=trade_id,
            schedule=schedule,
            actual_order_model=actual_order_model,
            instruments=None if "instrument" not in transaction else transaction["instrument"],
            interest=None if "interest" not in transaction else transaction["interest"],
            order_id=None if "order_id" not in transaction else transaction["order_id"],
            pl=None if "pl" not in transaction else transaction["pl"],
            units=0 if "units" not in transaction else transaction["units"],
            side=None if "side" not in transaction else transaction["side"],
            expiry=None if "expiry" not in transaction else timeutils.convert_timestamp2datetime(transaction["expiry"]),
            price=0 if "price" not in transaction else transaction["price"],
            upperBound=0 if "upperBound" not in transaction else transaction["upperBound"],
            lowerBound=0 if "lowerBound" not in transaction else transaction["lowerBound"],
            stopLoss=0 if "stopLoss" not in transaction else transaction["stopLossPrice"],
            type=self.transaction_type_key(transaction["type"]),
            reason=0 if "reason" not in transaction else self.transaction_reason_key(transaction["reason"]),
            time=timeutils.convert_timestamp2datetime(transaction["time"]),
        )
        transaction_model.save()

    def transaction_type_key(self, value):
        for item in TRANSACTION_TYPE:
            if item[1] == value:
                return item[0]
        raise Exception('no constant for type.')

    def transaction_reason_key(self, value):
        for item in TRANSACTION_REASON:
            if item[1] == value:
                return item[0]
        raise Exception('no constant for reason.')

    def transaction_type_value(self, key):
        for item in TRANSACTION_TYPE:
            if item[0] == key:
                return item[1]
        raise Exception('no constant for type.')

    def transaction_reason_value(self, key):
        for item in TRANSACTION_REASON:
            if item[0] == key:
                return item[1]
        raise Exception('no constant for reason.')