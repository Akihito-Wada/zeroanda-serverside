from django.db import models

# Create your models here.

class ScheduleModel(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    title       = models.CharField(max_length=200)
    country     = models.CharField(max_length=200)
    priority    = models.IntegerField(default=0)
    target      = models.BooleanField(default=True)
    # available   = models.BooleanField(default=True)
    presentation_time   = models.DateTimeField()

