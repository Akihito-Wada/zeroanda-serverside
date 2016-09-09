from django.http    import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from zeroanda.constant import INSTRUMENTS, CALENDER_PERIOD
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.calender import CalenderProxyModel
from zeroanda   import utils

@csrf_exempt
def test_api_calender(request):
    accountModel = AccountProxyModel().get_account()
    proxy = CalenderProxyModel()
    result = proxy.get_calenders(INSTRUMENTS[2][0], CALENDER_PERIOD.ONE_WEEK.value)
    return HttpResponse('200')

