from operator import attrgetter

from zeroanda.classes.utils import timeutils
from zeroanda.constant import TRANSACTION_TYPE, TRANSACTION_REASON
from zeroanda.models import TransactionModel
from zeroanda.proxy.streaming import Streaming
from zeroanda   import utils

class TransactionsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_transactions(self, account_id=None, instrument=None, id = None, ids = None, count = None, max_id = None, min_id = None, etag = None, actual_order_model_id=None):
        if actual_order_model_id != None:
            return TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id)
        else:
            try:
                transactionList = []
                response = self._streaming.get_transactions(account_id=account_id,instrument=instrument, id=id, ids=ids, count=count, max_id=max_id, min_id=min_id, etag=etag)
                if response.get_code() == 200:
                    if 'transactions' not in response.get_body():
                        return transactionList.append(TransactionValueObject(response.get_body()))
                    else:
                        transactions = response.get_body()["transactions"]
                        for transaction in transactions:
                            vo = TransactionValueObject(transaction)
                            transactionList.append(vo)
                        return sorted(transactionList, key=attrgetter('id'), reverse=True)
                else:
                    return None
            except:
                return None

    def get_latest_transaction_by_id(self, actual_order_model_id):
        try:
            return TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id).order_by('-id')[:1][0]
        except:
            return None

    def get_latest_type(self, actual_order_model_id):
        try:
            model = TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id).order_by('-id')[:1][0]
            return self.__transaction_type_value(model.type)
        except:
            return None

    def get_latest_transaction_reason_value(self, actual_order_model_id):
        try:
            model = TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id).order_by('-id')[:1][0]
            return self.__transaction_reason_value(model.reason)
        except:
            return None

    def add(self, transaction, trade_id=0, schedule=None, actual_order_model=None):
        transaction_model = TransactionModel(
            actual_order_id=transaction["id"],
            trade_id=trade_id,
            schedule=schedule,
            actual_order_model=actual_order_model,
            instruments=None if "instrument" not in transaction else transaction["instrument"],
            interest=0 if "interest" not in transaction else transaction["interest"],
            order_id=0 if "order_id" not in transaction else transaction["order_id"],
            pl=0 if "pl" not in transaction else transaction["pl"],
            units=0 if "units" not in transaction else transaction["units"],
            side=None if "side" not in transaction else transaction["side"],
            expiry=None if "expiry" not in transaction else timeutils.convert_timestamp2datetime(transaction["expiry"]),
            price=0 if "price" not in transaction else transaction["price"],
            upperBound=0 if "upperBound" not in transaction else transaction["upperBound"],
            lowerBound=0 if "lowerBound" not in transaction else transaction["lowerBound"],
            stopLoss=0 if "stopLoss" not in transaction else transaction["stopLossPrice"],
            type=self.__transaction_type_key(transaction["type"]),
            reason=0 if "reason" not in transaction else self.__transaction_reason_key(transaction["reason"]),
            time=timeutils.convert_timestamp2datetime(transaction["time"]),
        )
        transaction_model.save()

    def __transaction_type_key(self, value):
        for item in TRANSACTION_TYPE:
            if item[1] == value:
                return item[0]
        raise Exception('no constant for type.')

    def __transaction_reason_key(self, value):
        for item in TRANSACTION_REASON:
            if item[1] == value:
                return item[0]
        raise Exception('no constant for reason.')

    def __transaction_type_value(self, key):
        for item in TRANSACTION_TYPE:
            if item[0] == key:
                return item[1]
        raise Exception('no constant for type.')

    def __transaction_reason_value(self, key):
        for item in TRANSACTION_REASON:
            if item[0] == key:
                return item[1]
        raise Exception('no constant for reason.')

class TransactionValueObject:
    id          = None
    side        = None
    accountId   = None
    tradeId     = None
    orderId     = None
    reason      = None
    instrument  = None
    type        = None
    units       = None
    time        = None
    expiry      = None
    price       = None
    interest    = None
    pl          = None
    accountBalance  = None
    takeProfitPrice = None
    stopLossPrice   = None
    upperBound      = None
    lowerBound      = None
    tradeReducedId  = None
    tradeReducedPl  = None
    tradeReducedUnits   = None
    tradeReducedInterest    = None
    tradeOpenedId           = None
    tradeOpenedUnits        = None

    def __init__(self, response):
        self.id          = response["id"]
        self.accountId   = response["accountId"]
        self.type        = response["type"]
        self.time        = timeutils.convert_timestamp2datetime(response["time"])

        self.orderId     = 0 if "orderId" not in response else response["orderId"]
        self.reason      = None if "reason" not in response else response["reason"]
        self.units       = 0 if "units" not in response else response["units"]
        self.instrument  = None if "instrument" not in response else response["instrument"]
        self.side        = None if "side" not in response else response["side"]
        self.tradeId     = 0 if "tradeId" not in response else response["tradeId"]
        self.expiry      = 0 if "expiry" not in response else timeutils.convert_timestamp2datetime(response["expiry"])
        self.price       = 0 if "price" not in response else response["price"]
        self.interest    = 0 if "interest" not in response else response["interest"]
        self.pl          = 0 if "pl" not in response else response["pl"]
        self.accountBalance  = 0 if "accountBalance" not in response else response["accountBalance"]
        self.takeProfitPrice = 0 if "takeProfitPrice" not in response else response["takeProfitPrice"]
        self.stopLossPrice   = 0 if "stopLossPrice" not in response else response["stopLossPrice"]
        self.upperBound      = 0 if "upperBound" not in response else response["upperBound"]
        self.lowerBound      = 0 if "lowerBound" not in response else response["lowerBound"]
        self.tradeReducedId  = 0 if "tradeReduced" not in response or "id" not in response["tradeReduced"] else response["tradeReduced"]["id"]
        self.tradeReducedPl  = 0 if "tradeReduced" not in response or "pl" not in response["tradeReduced"] else response["tradeReduced"]["pl"]
        self.tradeReducedUnits   = 0 if "tradeReduced" not in response or "units" not in response["tradeReduced"] else response["tradeReduced"]["units"]
        self.tradeReducedInterest    = 0 if "tradeReduced" not in response or "interest" not in response["tradeReduced"] else response["tradeReduced"]["interest"]
        self.tradeOpenedId           = 0 if "tradeOpened" not in response or "id" not in response["tradeOpened"] else response["tradeOpened"]["id"]
        self.tradeOpenedUnits        = 0 if "tradeOpened" not in response or "units" not in response["tradeOpened"] else response["tradeOpened"]["units"]