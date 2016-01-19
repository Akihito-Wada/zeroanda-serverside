from django.http    import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache

from zeroanda.models import ScheduleModel

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

import  logging

logger =logging.getLogger("django")

# class Order(APIView):
#     @csrf_exempt
#     @never_cache
#     def get(self, request):
#         logger.info('get')
#         return HttpResponse('')
#
#     @csrf_exempt
#     @never_cache
#     def post(self, request, format=None):
#         logger.info(request["schedule_id"])
#         return HttpResponse('')
#
#     def get_object(self, pk):
#         try:
#             return ScheduleModel.objects.get(pk=pk)
#         except ScheduleModel.DoesNotExist:
#             raise Http404

@csrf_exempt
def order(request):
    if request.method == 'GET':
        logger.info('get')
    elif request.method == 'POST':
        logger.info(request.POST["schedule_id"])
    return HttpResponse('200')
