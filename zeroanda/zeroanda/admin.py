from datetime import datetime, timezone, timedelta
from django.utils   import dateformat
from django.contrib import admin
from zeroanda.models import ScheduleModel, ProcessModel, PricesModel, OrderModel, ErrorModel, AccountModel
from zeroanda import utils

class OrderModelAdmin(admin.StackedInline):
    model = OrderModel
    extra = 0
    readonly_fields = ('update_time',)

    def update_time(self, instance):
        return utils.format_jst(instance.updated)

class ScheduleModelAdmin(admin.ModelAdmin):
    change_form_template = 'zeroanda/schedule/change_form.html'
    
    list_display = ('title','presentation_time')
    inlines = [OrderModelAdmin]

class ProcessModelAdmin(admin.ModelAdmin):
    list_display = ('pid',)
    readonly_fields = ('schecule_title', 'pid', 'status', 'schedule_presentation_time', 'created_time', 'end_time',)

    def schecule_title(self, instance):
        return instance.schedule.title

    def schedule_presentation_time(self, instance):
        return utils.format_jst(instance.schedule.presentation_time)

    def created_time(self, instance):
        return utils.format_jst(instance.created)

    def end_time(self, instance):
        return utils.format_jst(instance.endtime)

class PriceModelAdmin(admin.ModelAdmin):
    list_display = ('schecule_title', 'instrument', 'ask', 'bid','begin_time',
                    # 'elapsed'
                    )
    readonly_fields = ('schecule_title',
                       'schedule_presentation_time',
                       'ask',
                       'bid',
                       'instrument',
                       'target_server_time',
                       'begin_time',
                       'end_time',
                       'elapsed',
                       'created_time',
                       )

    def schecule_title(self, instance):
        return instance.schedule.title

    def schedule_presentation_time(self, instance):
        return utils.format_jst(instance.schedule.presentation_time)

    def created_time(self, instance):
        return utils.format_jst(instance.created)

    def target_server_time(self, instance):
        return utils.format_jst(instance.time)

    def begin_time(self, instance):
        return utils.format_jst(instance.begin)

    def end_time(self, instance):
        return utils.format_jst(instance.end)

class ErrorModelAdmin(admin.ModelAdmin):
    list_display = ('code', 'message', 'created_time')
    readonly_fields = ('code', 'message', 'info', 'created_time')

    def created_time(self, instance):
        return utils.format_jst(instance.created)

class AccountModelAdmin(admin.ModelAdmin):
    list_display = ('account_id',
                    'margin_rate',
                    'account_currency',
                    'account_name',
                    'created_time')
    readonly_fields = ('account_id',
                       'margin_rate',
                       'margin_used',
                       'margin_avail',
                       'open_orders',
                       'open_trades',
                       'unrealized_pl',
                       'realized_pl',
                       'balance',
                       'account_currency',
                       'account_name',
                       'created_time',
                       'updated_time')

    def created_time(self, instance):
        return utils.format_jst(instance.created)

    def updated_time(self, instance):
        return utils.format_jst(instance.updated)

admin.site.register(ScheduleModel, ScheduleModelAdmin)
admin.site.register(ProcessModel, ProcessModelAdmin)
admin.site.register(PricesModel, PriceModelAdmin)
admin.site.register(ErrorModel, ErrorModelAdmin)
admin.site.register(AccountModel, AccountModelAdmin)