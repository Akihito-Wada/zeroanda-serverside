from django.http    import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from zeroanda.constant import INSTRUMENTS
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.events import EventsProxyModel

from zeroanda   import utils
from zeroanda.classes.utils import timeutils

@csrf_exempt
def test_api_events(request):
    if request.method == 'GET':

        accountModel = AccountProxyModel().get_account()
        eventModel = EventsProxyModel()
        result = eventModel.get_events(account_id=accountModel.account_id)
        utils.info(result.get_body())

        return HttpResponse('200')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET',])
