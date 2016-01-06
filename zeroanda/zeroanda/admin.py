from datetime import datetime, timezone, timedelta
from django.utils   import dateformat
from django.contrib import admin
from zeroanda.models import ScheduleModel, ProcessModel, PricesModel
from zeroanda import utils

class ScheduleModelAdmin(admin.ModelAdmin):
    list_display = ('title','presentation_time')

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
    list_display = ('schecule_title', 'instrument', 'ask', 'bid','begin_time')
    readonly_fields = ('schecule_title',
                       'schedule_presentation_time',
                       'ask',
                       'bid',
                       'instrument',
                       'target_server_time',
                       'begin_time',
                       'end_time',
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

admin.site.register(ScheduleModel, ScheduleModelAdmin)
admin.site.register(ProcessModel, ProcessModelAdmin)
admin.site.register(PricesModel, PriceModelAdmin)