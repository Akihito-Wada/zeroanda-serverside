from django.http    import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from zeroanda.controller.process import OrderProcess
from zeroanda   import utils

from datetime import datetime, timedelta

@csrf_exempt
def test_api_process_countdown(request):
    orderProcess = OrderProcess()
    targetdate = datetime.now() + timedelta(seconds=10)
    orderProcess.countdown(targetdate, test_exec)
    return HttpResponse('200')

def test_exec():
    utils.info('test_exec')

