from django.http    import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from zeroanda.constant import INSTRUMENTS, CALENDER_PERIOD
from zeroanda.proxy.calender import CalenderProxyModel
from zeroanda.proxy.schedule import ScheduleProxyModel

from zeroanda.services.economic_indicator.economic_indicator_service import EconomicInidcatorService

from zeroanda   import utils

@csrf_exempt
def test_api_calender(request):
    proxy = CalenderProxyModel()
    result = proxy.get_calenders(INSTRUMENTS[2][0], CALENDER_PERIOD.ONE_WEEK.value)
    return HttpResponse('200')


@csrf_exempt
def test_api_csv(request):
    service = EconomicInidcatorService()
    service.getsom()
    # proxy = ScheduleProxyModel()
    # result = proxy.get_economic_indicator()
    return HttpResponse('200')

