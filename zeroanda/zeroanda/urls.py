"""zeroanda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from zeroanda.api import order, cancel, cancelAll, prices, tick, ifdoco
from zeroanda.views import TradeListView, PositionListView

from zeroanda.test.test_api_positions import test_api_positions
from zeroanda.test.test_api_trades import test_api_trades
from zeroanda.test.test_api_orders import test_order_buy_market, test_api_orders
from zeroanda.test.test_api_account import test_api_account
from zeroanda.test.test_api_process import test_api_process_countdown

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include("api.urls")),
    url(r'^', include('snippets.urls')),
    url(r'^zeroanda/api/order$', order),
    url(r'^zeroanda/api/order/ifdoco$', ifdoco),
    url(r'^zeroanda/api/order/cancel$', cancel),
    url(r'^zeroanda/api/order/cancelall$', cancelAll),
    url(r'^zeroanda/api/prices', prices),
    url(r'^zeroanda/api/tick', tick),
    url(r'^zeroanda/orders$', TradeListView.as_view()),
    url(r'^zeroanda/position', PositionListView.as_view()),

    url(r'^zeroanda/test/orders', test_api_orders),
    url(r'^zeroanda/test/order/buy_market', test_order_buy_market),
    url(r'^zeroanda/test/trades', test_api_trades),
    url(r'^zeroanda/test/positions', test_api_positions),
    url(r'^zeroanda/test/accounts', test_api_account),
    url(r'^zeroanda/test/process', test_api_process_countdown),

]

urlpatterns += staticfiles_urlpatterns()