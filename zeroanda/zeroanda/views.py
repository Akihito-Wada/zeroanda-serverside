from django.views   import generic

from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.account import AccountProxyModel

from zeroanda import utils

class TradesListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
        result = orderClass.get_orders(accountModel)
        utils.info(result)
        context = super(TradesListView, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        return 'zeroanda/ticket/change_list.html'

class PositionsListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        accountModel = AccountProxyModel().get_account()

        orderClass = OrderProxyModel()
        orderClass.positions(accountModel)

        context = super(PositionsListView, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        return 'zeroanda/ticket/change_list.html'