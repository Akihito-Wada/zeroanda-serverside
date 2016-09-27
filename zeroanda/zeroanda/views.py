from datetime import timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views   import generic

from operator import attrgetter

from zeroanda.classes.utils import timeutils
from zeroanda.constant import SCHEDULE_STATUS, SCHEDULE_AVAILABLE, SIDE, INSTRUMENTS
from zeroanda.models import TradeTransactionModel, TradeModel, ScheduleModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda.proxy.setting import SettingProxy
from zeroanda.proxy.transactions import TransactionsProxyModel

from zeroanda import utils

class OrdersListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        context = super(OrdersListView, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        return 'zeroanda/ticket/change_list.html'

class PositionListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        accountModel = AccountProxyModel().get_account()

        orderClass = OrderProxyModel()
        orderClass.positions(accountModel)

        context = super(PositionListView, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        return 'zeroanda/position/change_list.html'

class PriceListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        priceModel  = PricesProxyModel.get_price()

        context = super(PriceListView, self).get_context_data()
        return context

    def get_template_names(self):
        return 'zeroanda/prices/change_list.html'


class TradeListView(generic.ListView):
    context_object_name = "trade_list"

    def get_queryset(self):
        return TradeModel.objects.all().order_by("-created")

    def get_template_names(self):
        return 'zeroanda/trades/change_list.html'


class TransactionListView(generic.ListView):
    context_object_name = "transaction_list"

    def get_queryset(self):
        for key, value in self.request.GET.items():
            utils.info(key)
        return TradeTransactionModel.objects.all().order_by("-created")

    def get_template_names(self):
        return 'zeroanda/transactions/change_list.html'

class TransactionsView(generic.ListView):
    context_object_name = "transactions"

    def get_queryset(self):
        accountModel = AccountProxyModel().get_account()
        transactionModel = TransactionsProxyModel()
        result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], count=50)
        return result

    def get_template_names(self):
        return 'zeroanda/transactions/list.html'

@login_required
def transaction_list(request, trade_id):
    if request.method == 'GET':
        tradeModel = TradeModel.objects.get(pk=trade_id)
        if tradeModel != None:
            scheduleModel = ScheduleModel.objects.get(pk=tradeModel.schedule.id)
            schedule_available = SCHEDULE_AVAILABLE[scheduleModel.target][1]
            schedule_status = SCHEDULE_STATUS[scheduleModel.status][1]

            accountProxy = AccountProxyModel()
            accountModel = accountProxy.get_account()
            accountInfoModel = accountProxy.get_account_info()

            priceProxyModel = PricesProxyModel()
            priceModel = priceProxyModel.get_price(trade_id=trade_id)

            startdate = scheduleModel.presentation_time +  timedelta(seconds=settings.DURATION_IFDOCO_EXCUTE_TIME - 10)
            enddate = scheduleModel.presentation_time + timedelta(seconds=SettingProxy.get_expire_time(scheduleModel.priority) + 20)
            price_list = priceProxyModel.get_candles(scheduleModel.instrument, timeutils.convert_rfc2unixtime(startdate), timeutils.convert_rfc2unixtime(enddate))
            if price_list is not None:
                for price in price_list['candles']:
                    price['time'] = timeutils.format_unixtime_to_jst(timeutils.format_unixtime(price['time']))

            orderProxyModel = OrderProxyModel()
            orderModelSell = orderProxyModel.get_order_by_trade_id(trade_id=trade_id, side=SIDE[0][0])
            orderModelBuy = orderProxyModel.get_order_by_trade_id(trade_id=trade_id, side=SIDE[1][0])
            transactionModel = TransactionsProxyModel()

            sell_transaction_list = None
            buy_transaction_list = None
            if orderModelSell != None and orderModelBuy != None:
                min_id = orderModelBuy.actual_order_id if orderModelBuy.actual_order_id < orderModelSell.actual_order_id else orderModelSell.actual_order_id
                utils.info('min_id')
                utils.info(min_id)
                transactions = transactionModel.get_transactions(account_id=accountModel.account_id,
                                                                 instrument=scheduleModel.instrument, min_id=min_id)
                utils.info('transactions')
                utils.info(transactions)
                buy_transaction_list = __sort_out_transaction(transactions, orderModelBuy.actual_order_id)
                sell_transaction_list = __sort_out_transaction(transactions, orderModelSell.actual_order_id)


        transaction_list = TradeTransactionModel.objects.filter(trade_model_id=trade_id).order_by("created")
        return render(request, 'zeroanda/transactions/change_list.html',
                      {
                          'transaction_list': transaction_list,
                          'trade_model': tradeModel,
                          'schedule_model': scheduleModel,
                          'schedule_available': schedule_available,
                          'schedule_status': schedule_status,
                          'account_model': accountModel,
                          'account_info_model': accountInfoModel,
                          'price_model': priceModel,
                          'order_model_sell': orderModelSell,
                          'order_model_buy': orderModelBuy,
                          'price_list': price_list,
                          'buy_transaction_list': buy_transaction_list,
                          'sell_transaction_list': sell_transaction_list,
                      })
    return HttpResponse('200')

def __sort_out_transaction(transaction_list, actual_transaction_id):
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
            __sort_out_transaction_by_trade_id(target_list, transaction_list, transaction.id)
    return sorted(target_list, key=attrgetter('id'))


def __sort_out_transaction_by_trade_id(return_list, transaction_list, target_transaction_id):
    for transaction in transaction_list:
        if target_transaction_id == transaction.tradeId:
            return_list.append(transaction)
    return return_list