from django.http    import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from zeroanda.constant import INSTRUMENTS
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.transactions import TransactionsProxyModel

from zeroanda   import utils

@csrf_exempt
def test_api_transactions(request):
    if request.method == 'GET':

        accountModel = AccountProxyModel().get_account()
        transactionModel = TransactionsProxyModel()
        result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], count=2)
        utils.info(result)

        return HttpResponse('200')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET',])
