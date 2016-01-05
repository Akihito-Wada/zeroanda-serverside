from django.contrib import admin
from zeroanda.models import ScheduleModel

class ScheduleModelAdmin(admin.ModelAdmin):
    list_display = ('title','presentation_time')

admin.site.register(ScheduleModel, ScheduleModelAdmin)