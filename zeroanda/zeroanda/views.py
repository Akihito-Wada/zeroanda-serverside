from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views   import generic

from zeroanda.models import TransactionModel, TradeModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.prices import PricesProxyModel

from zeroanda import utils

class OrdersListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
        result = orderClass.get_orders(accountModel)
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
        utils.info(333)
        for key, value in self.request.GET.items():
            utils.info(key)
        utils.info(self.request.GET)
        utils.info(self.request.GET.get('trade_id'))
        return TransactionModel.objects.all().order_by("-created")

    def get_template_names(self):
        return 'zeroanda/transactions/change_list.html'

def transaction_list(request, trade_id):
    utils.info(333)
    if request.method == 'GET':
        utils.info(trade_id)
        transaction_list = TransactionModel.objects.filter(trade_model_id=trade_id).order_by("created")
        return render(request, 'zeroanda/transactions/change_list.html', {'transaction_list': transaction_list})
    return HttpResponse('200')