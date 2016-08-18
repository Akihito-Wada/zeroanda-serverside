from datetime import timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views   import generic

from zeroanda.classes.utils import timeutils
from zeroanda.constant import SCHEDULE_STATUS, SCHEDULE_AVAILABLE, SIDE, INSTRUMENTS
from zeroanda.models import TradeTransactionModel, TradeModel, ScheduleModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda.proxy.transactions import TransactionsProxyModel

from zeroanda import utils

class OrdersListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
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
        result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], count=20)
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

            startdate = scheduleModel.presentation_time +  timedelta(seconds=settings.DURATION_IFDOCO_EXCUTE_TIME - 1)
            enddate = scheduleModel.presentation_time + timedelta(seconds=settings.EXPIRY_SECONDS + 1)
            price_list = priceProxyModel.get_candles(scheduleModel.country, timeutils.convert_rfc2unixtime(startdate), timeutils.convert_rfc2unixtime(enddate))
            for price in price_list['candles']:
                price['time'] = timeutils.format_unixtime_to_jst(timeutils.format_unixtime(price['time']))

            orderProxyModel = OrderProxyModel()
            orderModelSell = orderProxyModel.get_order_by_trade_id(trade_id=trade_id, side=SIDE[0][0])
            orderModelBuy = orderProxyModel.get_order_by_trade_id(trade_id=trade_id, side=SIDE[1][0])

            transactionModel = TransactionsProxyModel()

            if orderModelBuy != None and orderModelBuy.actual_model != None:
                type_buy = transactionModel.get_latest_type(orderModelBuy.actual_model.id)
                reason_buy = transactionModel.get_latest_transaction_reason_value(orderModelBuy.actual_model.id)
                buy_latest_transaction = transactionModel.get_latest_transaction_by_id(orderModelBuy.actual_model.id)
            else:
                type_buy = None
                reason_buy = None

            if orderModelSell != None and orderModelSell.actual_model != None:
                type_sell = transactionModel.get_latest_type(orderModelSell.actual_model.id)
                reason_sell = transactionModel.get_latest_transaction_reason_value(orderModelSell.actual_model.id)
                sell_latest_transaction = transactionModel.get_latest_transaction_by_id(orderModelSell.actual_model.id)
            else:
                type_sell = None
                reason_sell = None

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
                          'buy_latest_transaction': buy_latest_transaction,
                          'sell_latest_transaction': sell_latest_transaction,
                          'type_buy': type_buy,
                          'reason_buy': reason_buy,
                          'type_sell': type_sell,
                          'reason_sell': reason_sell,
                          'price_list': price_list,
                      })
    return HttpResponse('200')