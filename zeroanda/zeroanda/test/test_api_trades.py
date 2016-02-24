import  logging

from django.http    import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from zeroanda   import utils
from zeroanda.controller.process import OrderProcess
from zeroanda.errors import ZeroandaError
from zeroanda.models import ScheduleModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda.proxy.schedule import ScheduleProxyModel

from zeroanda.constant import INSTRUMENTS

@csrf_exempt
def test_api_trades(request):
    utils.info(request.method)

    if request.method == 'GET':
        return HttpResponse('200')
    elif request.method == 'POST':
        return HttpResponse('200')
    elif request.method == 'PATCH':
        # accountModel = AccountProxyModel().get_account()
        # orderClass = OrderProxyModel()
        # orders = orderClass.buy_market(accountModel, INSTRUMENTS[0][0], 1)
        # utils.info(orders)
        return HttpResponse('200')
    elif request.method == 'DELETE':
        return HttpResponse('200')
    else:
        return HttpResponse('403')
