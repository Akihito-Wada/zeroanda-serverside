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
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
        orderClass.get_orders(accountModel)
        # orderClass.traders(accountModel)
    elif request.method == 'POST':
        try:
            model = ScheduleModel.objects.get(pk=request.POST.get("schedule_id"))
            OrderProcess.create(model).test_order_buy()

        except ZeroandaError as e:
            print('error')
            e.save()
    return HttpResponse('200')

@csrf_exempt
def cancel(request):
    id = request.POST.get('actual_order_id')

    if id == None:
        return HttpResponse(404)
    else:
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
        orderClass.cancel(accountModel, id)
        return HttpResponse('200')

@csrf_exempt
def cancelAll(request):
    accountModel = AccountProxyModel().get_account()
    orderClass = OrderProxyModel()
    orderClass.cancel_all(accountModel)
    return HttpResponse('200')