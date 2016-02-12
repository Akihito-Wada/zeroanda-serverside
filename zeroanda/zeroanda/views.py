from django.views   import generic

from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.prices import PricesProxyModel

from zeroanda import utils

class TradeListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
        result = orderClass.get_orders(accountModel)
        utils.info(result)
        context = super(TradeListView, self).get_context_data(**kwargs)
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