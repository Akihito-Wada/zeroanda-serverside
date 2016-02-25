import  logging

from django.http    import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from zeroanda   import utils
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.trades import TradesProxyModel

@csrf_exempt
def test_api_trades(request):
    utils.info(request.method)

    if request.method == 'GET':
        accountModel = AccountProxyModel().get_account()
        tradesProxyModel = TradesProxyModel();
        tradesProxyModel.get_trades(accountModel)

        return HttpResponse('200')
    elif request.method == 'POST':
        return HttpResponseNotAllowed(permitted_methods=['GET', 'PATCH', 'DELETE'])
    elif request.method == 'PATCH':
        return HttpResponse('200')

    elif request.method == 'DELETE':
        trade_id='10128286273'
        accountModel = AccountProxyModel().get_account()
        tradesProxyModel = TradesProxyModel();
        tradesProxyModel.close_trades(accountModel, trade_id)
        return HttpResponse('200')
    else:
        return HttpResponse('403')
