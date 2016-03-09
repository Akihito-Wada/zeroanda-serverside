import  logging

from django.http    import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from zeroanda   import utils
from zeroanda.proxy.positions import PositionsProxyModel
from zeroanda.proxy.account import AccountProxyModel

@csrf_exempt
def test_api_positions(request):
    utils.info(request.method)

    if request.method == 'GET':
        accountModel = AccountProxyModel().get_account()
        positions = PositionsProxyModel();
        positions.get_positions(accountModel)
        return HttpResponse('200')

    elif request.method == 'DELETE':
        return HttpResponseNotAllowed(permitted_methods=['GET',])

        accountModel = AccountProxyModel().get_account()
        positions = PositionsProxyModel();
        positions.delete_positions(accountModel)
        return HttpResponse('200')

    else:
        return HttpResponse('403')