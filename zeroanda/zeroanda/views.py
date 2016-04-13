from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views   import generic

from zeroanda.constant import SCHEDULE_STATUS, SCHEDULE_AVAILABLE, SIDE
from zeroanda.models import TransactionModel, TradeModel, ScheduleModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.prices import PricesProxyModel

from zeroanda import utils

class OrdersListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
        result = orderClass.get_orders(accountModel.account_id)
        utils.info(result)
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
        return TransactionModel.objects.all().order_by("-created")

    def get_template_names(self):
        return 'zeroanda/transactions/change_list.html'

def transaction_list(request, trade_id):
    if request.method == 'GET':
        tradeModel = TradeModel.objects.get(pk=trade_id)
        if tradeModel != None:
            scheduleModel = ScheduleModel.objects.get(pk=tradeModel.schedule.id)
            schedule_available = SCHEDULE_AVAILABLE[scheduleModel.target][1]
            schedule_status = SCHEDULE_STATUS[scheduleModel.status][1]

            priceProxyModel = PricesProxyModel()
            priceModel = priceProxyModel.get_price(trade_id=trade_id)

            orderProxyModel = OrderProxyModel()
            orderModelSell = orderProxyModel.get_order_by_trade_id(trade_id=trade_id, side=SIDE[0][0])
            orderModelBuy = orderProxyModel.get_order_by_trade_id(trade_id=trade_id, side=SIDE[1][0])

        transaction_list = TransactionModel.objects.filter(trade_model_id=trade_id).order_by("created")
        return render(request, 'zeroanda/transactions/change_list.html',
                      {
                          'transaction_list': transaction_list,
                          'trade_model': tradeModel,
                          'schedule_model': scheduleModel,
                          'schedule_available': schedule_available,
                          'schedule_status': schedule_status,
                          'price_model': priceModel,
                          'order_model_sell': orderModelSell,
                          'order_model_buy': orderModelBuy,
                      })
    return HttpResponse('200')