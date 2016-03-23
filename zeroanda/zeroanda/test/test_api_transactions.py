from django.http    import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from zeroanda.constant import INSTRUMENTS
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.transactions import TransactionsProxyModel

from zeroanda   import utils
from zeroanda.classes.utils import timeutils

@csrf_exempt
def test_api_transactions(request):
    if request.method == 'GET':

        accountModel = AccountProxyModel().get_account()
        transactionModel = TransactionsProxyModel()
        etag = "df8446ef2ea9a10ac34216ce287b79e9e7d9e72d"
        ids = '10190778803,10190778800'
        result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], count=2)
        # result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], ids=ids)
        # result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], ids=ids, etag=etag)
        utils.info(result.get_body())
        utils.info(timeutils.convert_timestamp2datetime(result.get_body()["transactions"][0]['expiry']))

        return HttpResponse('200')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET',])
