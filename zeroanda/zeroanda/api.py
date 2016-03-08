import  logging

from django.http    import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from zeroanda   import utils
from zeroanda.constant import INSTRUMENTS
from zeroanda.controller.process import OrderProcess
from zeroanda.errors import ZeroandaError
from zeroanda.models import ScheduleModel
from zeroanda.proxy.account import AccountProxyModel
from zeroanda.proxy.order import OrderProxyModel
from zeroanda.proxy.prices import PricesProxyModel
from zeroanda.proxy.schedule import ScheduleProxyModel

logger =logging.getLogger("django")

@csrf_exempt
def order(request):
    if request.method == 'GET':
        accountModel = AccountProxyModel().get_account()
        orderClass = OrderProxyModel()
        orders = orderClass.get_orders(accountModel)
        utils.info(orders)
    elif request.method == 'POST':
        try:
            scheduleModel = ScheduleModel.objects.get(pk=request.POST.get("schedule_id"))
            priceModel = PricesProxyModel(scheduleModel)
            price = priceModel.get_price()
            OrderProcess.create(scheduleModel).test_order_buy(price.ask + 10)

        except ZeroandaError as e:
            print('error')
            e.save()
    # elif request.method == 'DELETE':

    return HttpResponse('200')

@csrf_exempt
def ifdoco(request):
    utils.info('test')
    if request.method == 'POST':
        # scheduleModel = ScheduleProxyModel().get_schedule(request.POST.get('schedule_id'))
        scheduleModel = ScheduleProxyModel().get_schedule(4)
        OrderProcess.create(scheduleModel).test_ifdoco()
        return HttpResponse('200')
    else:
        return HttpResponse('403')

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


@csrf_exempt
def prices(request):
    if request.method == 'GET':
        try:
            scheduleModel = ScheduleProxyModel().get_schedule(request.GET.get('schedule_id'))
            model = PricesProxyModel(scheduleModel)
            model.get_price()
            return HttpResponse('200')
        except Exception as e:
            utils.info(e)
            return HttpResponse('403')


@csrf_exempt
def tick(request):
    if request.method == 'GET':
        try:
            scheduleModel = ScheduleProxyModel().get_schedule(request.GET.get('schedule_id'))
            # model = PricesProxyModel(scheduleModel)
            # model.get_price()
            OrderProcess.create(scheduleModel).test_ticking_price()
            return HttpResponse('200')
        except Exception as e:
            utils.info(e)
            return HttpResponse('403')