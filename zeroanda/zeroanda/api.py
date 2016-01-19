import  logging

from django.http    import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from zeroanda.proxy.order import OrderProxyModel
from zeroanda.errors import ZeroandaError
from zeroanda.models import ScheduleModel
from zeroanda.process import OrderProcess
from zeroanda.proxy.account import AccountProxyModel

logger =logging.getLogger("django")


@csrf_exempt
def order(request):
    if request.method == 'GET':
        logger.info('get')
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
        # orderClass.get(accountModel)
        orderClass.traders(accountModel)
    elif request.method == 'POST':
        logger.info(request.POST["schedule_id"])
        try:
            model = ScheduleModel.objects.get(pk=request.POST["schedule_id"])
            OrderProcess.create(model).test_order_buy()

        except ZeroandaError as e:
            print('error')
            e.save()

    return HttpResponse('200')
