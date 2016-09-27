from operator import attrgetter

from zeroanda.proxy.transactions import TransactionsProxyModel
from zeroanda import utils

class TransactionService:
    def __init__(self):return

    def get_and_add_transactions(self, account_id, instrument, schedule, min_id, ask_order_model, bid_order_model, trade_id):
        utils.info('get_and_add_transactions')
        transactionProxy = TransactionsProxyModel()
        transactions = transactionProxy.get_transactions(account_id = account_id, instrument = instrument, min_id = min_id)
        utils.info('transactions')
        utils.info(transactions)
        buy_transaction_list = self.__sort_out_transaction(transactions, bid_order_model.actual_order_id)
        utils.info('buy_transaction_list')
        for transaction in buy_transaction_list:
            utils.info(transaction)
            transactionProxy.add(transaction, trade_id=trade_id, schedule=schedule, actual_order_model=bid_order_model)

        sell_transaction_list = self.__sort_out_transaction(transactions, ask_order_model.actual_order_id)
        utils.info('sell_transaction_list')
        for transaction in sell_transaction_list:
            utils.info(transaction)
            transactionProxy.add(transaction, trade_id=trade_id, schedule=schedule, actual_order_model=ask_order_model)

    def __sort_out_transaction(self, transaction_list, actual_transaction_id):
        target_list = []
        for transaction in transaction_list:
            if actual_transaction_id == transaction.id:
                target_list.append(transaction)
                break
        if len(target_list) == 0:
            return target_list
        for transaction in transaction_list:
            if target_list[0].id == transaction.orderId:
                target_list.append(transaction)
                self.__sort_out_transaction_by_trade_id(target_list, transaction_list, transaction.id)
        return sorted(target_list, key=attrgetter('id'))

    def __sort_out_transaction_by_trade_id(self, return_list, transaction_list, target_transaction_id):
        for transaction in transaction_list:
            if target_transaction_id == transaction.tradeId:
                return_list.append(transaction)
        return return_list