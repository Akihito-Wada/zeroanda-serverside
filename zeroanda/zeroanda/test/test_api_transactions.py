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
        ids = '10231579886,10231579885'
        id = '10233653978'
        # result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], count=2)
        result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], id=id)
        # result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], id=id, etag=etag)
        # result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], ids=ids)
        # result = transactionModel.get_transactions(accountModel.account_id, INSTRUMENTS[0][0], ids=ids, etag=etag)
        # utils.info(result.get_body())
        if result.get_code() == 429:
            return HttpResponse('200')
        if 'transactions' not in result.get_body():
            transactionModel.add(result.get_body())
        else:
            transactions = result.get_body()["transactions"]
            for transaction in transactions:
                transactionModel.add(result.get_body())
        # transaction = result.get_body() if 'transactions' not in result.get_body() else result.get_body()["transactions"][0]
        # utils.info(transaction)
        # if 'expiry' in transaction:
        #     utils.info(timeutils.convert_timestamp2datetime(transaction['expiry']))

        return HttpResponse('200')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET',])
