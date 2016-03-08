from django.http    import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from zeroanda   import utils

@csrf_exempt
def test_api_call_action(request):
    utils.info(33)
    if request.method == 'GET':
        test_call_action()
        return HttpResponse('200')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET',])

def test_call_action():
    utils.info('test_call_action')
    return