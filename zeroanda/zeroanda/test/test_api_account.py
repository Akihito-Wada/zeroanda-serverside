from django.http    import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from zeroanda   import utils
from zeroanda.proxy.account import AccountProxyModel

@csrf_exempt
def test_api_account(request):
    utils.info(request.method)

    if request.method == 'GET':
        accountProxyModel = AccountProxyModel()
        accountProxyModel.get_account_info()
        return HttpResponse('200')
    else :
        return HttpResponseNotAllowed(permitted_methods=['GET',])
