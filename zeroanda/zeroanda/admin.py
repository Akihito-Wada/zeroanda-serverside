from django.contrib import admin
from zeroanda.models import ScheduleModel, ProcessModel, PricesModel, OrderModel, ErrorModel, AccountModel, ActualOrderModel
from zeroanda import utils
from zeroanda.classes.utils import timeutils
from zeroanda.constant import ACTUAL_ORDER_STATUS

import logging
logger =logging.getLogger("django")

class ActualOrderModelAdmin(admin.StackedInline):
    model = ActualOrderModel
    exclude = ['schedule', 'expiry', 'time','updated']
    readonly_fields = (
        'actual_order_id',
        'instruments',
        'units',
        'side',
        'price',
        'upperBound',
        'lowerBound',
        'stopLoss',
        'takeProfit',
        'trailingStop',
        'error_code',
        'status',
        'created_time',
        'updated_date',
        'actual_datetime',
        'expiry_date',
        )

    def created_time(self, instance):
        return timeutils.format_jst(instance.created)
    def actual_datetime(self, instance):
        return timeutils.format_jst(instance.time)
    def expiry_date(self, instance):
        return timeutils.format_jst(instance.expiry)
    def updated_date(self, instance):
        return timeutils.format_jst(instance.updated)

class OrderModelAdmin(admin.ModelAdmin):
    _actualOrderModel = None
    change_form_template = 'zeroanda/admin/order/change_form.html'
    change_list_template = 'zeroanda/admin/order/change_list.html'
    # model = OrderModel
    # extra = 0
    exclude = ['expiry','updated']
    list_display = ('schedule', 'updated',)
    readonly_fields = (
        'id',
        'instruments',
        'side',
        'type',
        'expiry_time',
        'takeProfit',
        'traillingStop',
        'status',
        'created_time',
        'update_time',
    )
    inlines = [ActualOrderModelAdmin]

    def created_time(self, instance):
        return timeutils.format_jst(instance.created)

    def update_time(self, instance):
        return timeutils.format_jst(instance.updated)

    def expiry_time(self, instance):
        return timeutils.format_jst(instance.expiry)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        try :
            extra_context = extra_context or {}

            self._actualOrderModel= ActualOrderModel.objects.get(order=object_id)
            extra_context['actual_order_id'] = self._actualOrderModel.actual_order_id
        except ActualOrderModel.DoesNotExist as e:
            logger.error(e)
        finally:
            return super(OrderModelAdmin, self).change_view(request, object_id,
                form_url, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        if self._actualOrderModel == None or self._actualOrderModel.status != ACTUAL_ORDER_STATUS[0][0]:
            return (
                'id',
                'instruments',
                'units',
                'side',
                'type',
                'expiry_time',
                'price',
                'upperBound',
                'lowerBound',
                'stopLoss',
                'takeProfit',
                'traillingStop',
                'status',
                'created_time',
                'update_time',
            )
        else:
            return super(OrderModelAdmin, self).get_readonly_fields(request, obj)

class ScheduleModelAdmin(admin.ModelAdmin):
    change_form_template = 'zeroanda/admin/schedule/change_form.html'
    list_display = ('title','presentation_time')
    # inlines = [OrderModelAdmin]
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['schedule_model_id'] = object_id
        return super(ScheduleModelAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)

class ProcessModelAdmin(admin.ModelAdmin):
    list_display = ('pid',)
    readonly_fields = ('schecule_title', 'pid', 'status', 'schedule_presentation_time', 'created_time', 'end_time',)

    def schecule_title(self, instance):
        return instance.schedule.title

    def schedule_presentation_time(self, instance):
        return timeutils.format_jst(instance.schedule.presentation_time)

    def created_time(self, instance):
        return timeutils.format_jst(instance.created)

    def end_time(self, instance):
        return timeutils.format_jst(instance.endtime)

class PriceModelAdmin(admin.ModelAdmin):
    def created_time(self, instance):
        return timeutils.format_jst(instance.created)

    def target_server_time(self, instance):
        return timeutils.format_jst(instance.time)

    change_list_template = 'zeroanda/admin/price/change_list.html'
    # created_time.short_description = 'precise time'
    list_display = (
        'instrument',
        'ask',
        'bid',
        'created_time'
                 )
    # exclude = ('begin', 'time', 'end')
    readonly_fields = (
        # 'schecule_title',
        # 'schedule_presentation_time',
        'ask',
        'bid',
        'instrument',
        'etag',
        'target_server_time',
        # 'begin_time',
        # 'end_time',
        # 'elapsed',
        'created_time',
                       )

    # def schecule_title(self, instance):
    #     return instance.schedule.title

    def schedule_presentation_time(self, instance):
        return timeutils.format_jst(instance.schedule.presentation_time)

    # def begin_time(self, instance):
    #     return utils.format_jst(instance.begin)
    #
    # def end_time(self, instance):
    #     return utils.format_jst(instance.end)

class ErrorModelAdmin(admin.ModelAdmin):
    list_display = ('code', 'message', 'created_time')
    readonly_fields = ('code', 'message', 'info', 'created_time')

    def created_time(self, instance):
        return timeutils.format_jst(instance.created)

class AccountModelAdmin(admin.ModelAdmin):
    exclude = ['updated']
    list_display = ('account_id',
                    'margin_rate',
                    'account_currency',
                    'account_name',
                    'created_time')
    readonly_fields = ('account_id',
                       'margin_rate',
                       'etag',
                       # 'margin_used',
                       # 'margin_avail',
                       # 'open_orders',
                       # 'open_trades',
                       # 'unrealized_pl',
                       # 'realized_pl',
                       # 'balance',
                       'account_currency',
                       'account_name',
                       'created_time',
                       'updated_time')

    def created_time(self, instance):
        return timeutils.format_jst(instance.created)

    def updated_time(self, instance):
        return timeutils.format_jst(instance.updated)

admin.site.register(ScheduleModel, ScheduleModelAdmin)
admin.site.register(ProcessModel, ProcessModelAdmin)
admin.site.register(PricesModel, PriceModelAdmin)
admin.site.register(ErrorModel, ErrorModelAdmin)
admin.site.register(AccountModel, AccountModelAdmin)
admin.site.register(OrderModel, OrderModelAdmin)
