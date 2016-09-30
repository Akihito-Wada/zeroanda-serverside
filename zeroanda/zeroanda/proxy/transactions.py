from operator import attrgetter

from zeroanda.classes.net.streaming import Streaming
from zeroanda.classes.utils.loggerutils import Logger
from zeroanda.classes.utils import timeutils
from zeroanda.constant import TRANSACTION_TYPE, TRANSACTION_REASON
from zeroanda.models import TransactionModel
from zeroanda import utils

class TransactionsProxyModel:
    _streaming = None

    def __init__(self):
        self._streaming = Streaming()

    def get_transactions(self, account_id=None, instrument=None, id = None, ids = None, count = None, max_id = None, min_id = None, etag = None, actual_order_model_id=None, order_id=0, transaction_id=0, trade_id=0, actual_trade_id=0):
        if actual_order_model_id != None:
            return TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id)
        if order_id != 0:
            return TransactionModel.objects.filter(order_id=order_id)
        if transaction_id != 0:
            return TransactionModel.objects.filter(transaction_id=transaction_id)
        if trade_id != 0:
            return TransactionModel.objects.filter(trade_id=trade_id)
        if actual_trade_id != 0:
            return TransactionModel.objects.filter(actual_trade_id=actual_trade_id)
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
            return TransactionsProxyModel.transaction_type_value(model.type)
        except:
            return None

    def get_latest_transaction_reason_value(self, actual_order_model_id):
        try:
            model = TransactionModel.objects.filter(actual_order_model_id=actual_order_model_id).order_by('-id')[:1][0]
            return TransactionsProxyModel.transaction_reason_value(model.reason)
        except:
            return None

    def add(self, transaction, trade_id=0, schedule=None, actual_order_model=None):
        transaction_model   = TransactionModel(
            transaction_id = transaction.id,
            trade_id        = trade_id,
            schedule        = schedule,
            actual_order_model=actual_order_model,
            instruments     = transaction.instrument,
            interest        = transaction.interest,
            order_id        = transaction.orderId,
            actual_trade_id = transaction.tradeId,
            pl              = transaction.pl,
            units           = transaction.units,
            side            = transaction.side,
            expiry          = transaction.expiry,
            price           = transaction.price,
            account_balance=transaction.accountBalance,
            take_profit_price=transaction.takeProfitPrice,
            upper_bound      = transaction.upperBound,
            lower_bound      = transaction.lowerBound,
            stop_loss        = transaction.stopLossPrice,
            type            = TransactionsProxyModel.transaction_type_key(transaction.type),
            reason          = 0 if transaction.reason == None else TransactionsProxyModel.transaction_reason_key(transaction.reason),
            time            = transaction.time,
        )
        transaction_model.save()

    @staticmethod
    def transaction_type_key(value):
        for item in TRANSACTION_TYPE:
            if item[1] == value:
                return item[0]
        Logger.error("'no constant for type. value:{value}'".format(value=value))
        return TRANSACTION_TYPE[0][0]

    @staticmethod
    def transaction_reason_key(value):
        for item in TRANSACTION_REASON:
            if item[1] == value:
                return item[0]
        Logger.error("'no constant for reason. value:{value}'".format(value=value))
        return TRANSACTION_REASON[0][0]

    @staticmethod
    def transaction_type_value(key):
        for item in TRANSACTION_TYPE:
            if item[0] == key:
                return item[1]
        Logger.error("'no constant for type. value:{value}'".format(value=key))
        return TRANSACTION_TYPE[0][1]

    @staticmethod
    def transaction_reason_value(key):
        for item in TRANSACTION_REASON:
            if item[0] == key:
                return item[1]
        Logger.error("'no constant for reason. value:{value}'".format(value=key))
        return TRANSACTION_REASON[0][1]

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
        self.expiry      = None if "expiry" not in response else timeutils.convert_timestamp2datetime(response["expiry"])
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

    def __str__(self):
        return "id: {id}, account_id:{account_id}, type:{type}, time:{time}, orderId:{orderId}, reason:{reason}, units:{units}, instrument:{instrument}, side:{side}, tradeId:{tradeId}, expiry={expiry}, price:{price}, interest:{interest}, pl={pl}, accountBalance:{accountBalance}, takeProfitPrice:{takeProfitPrice}, stopLossPrice:{stopLossPrice}, upperBound:{upperBound}, lowerBound:{lowerBound}".format(id=self.id, account_id=self.accountId, instrument=self.instrument, orderId=self.orderId, side=self.side, price=self.price, interest=self.interest, pl=self.pl, upperBound=self.upperBound, lowerBound=self.lowerBound, units=self.units, takeProfitPrice=self.takeProfitPrice, stopLossPrice=self.stopLossPrice, expiry=self.expiry, type=self.type, reason=self.reason, time=self.time, tradeId=self.tradeId, accountBalance=self.accountBalance)