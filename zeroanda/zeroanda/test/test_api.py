from django.http    import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from zeroanda.constant import INSTRUMENTS, CALENDER_PERIOD
from zeroanda.proxy.calender import CalenderProxyModel
from zeroanda.proxy.schedule import ScheduleProxyModel
from zeroanda   import utils

@csrf_exempt
def test_api_calender(request):
    proxy = CalenderProxyModel()
    result = proxy.get_calenders(INSTRUMENTS[2][0], CALENDER_PERIOD.ONE_WEEK.value)
    return HttpResponse('200')


@csrf_exempt
def test_api_csv(request):
    proxy = ScheduleProxyModel()
    result = proxy.get_economic_indicator()
    return HttpResponse('200')

