import  logging

from django.http    import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from zeroanda   import utils
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.constant import INSTRUMENTS

@csrf_exempt
def test_api_orders(request):
    utils.info(request.method)

    if request.method == 'GET':
        try:
            accountModel = AccountProxyModel().get_account()
            orderProxyModel = OrderProxyModel()
            orderProxyModel.get_orders(accountModel)
            return HttpResponse('200')
        except :
            return HttpResponse(403)

    elif request.method == 'POST':
        return HttpResponse('200')

    elif request.method == 'PATCH':
        return HttpResponse('200')

    elif request.method == 'DELETE':
        try:
            order_id = 10155069789
            accountModel = AccountProxyModel().get_account()
            orderProxyModel = OrderProxyModel()
            orderProxyModel.cancel(accountModel, order_id)
            return HttpResponse('200')
        except :
            return HttpResponse(403)

    else:
        return HttpResponse('403')

@csrf_exempt
def test_order_buy_market(request):
    if request.method == 'POST':
        try:
            accountModel = AccountProxyModel().get_account()
            orderClass = OrderProxyModel()
            orders = orderClass.buy_market(accountModel, INSTRUMENTS[0][0], 1)
            utils.info(orders)
            return HttpResponse('200')
        except :
            return HttpResponse(403)
    else:
        return HttpResponse('403')
