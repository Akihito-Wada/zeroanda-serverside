from django.db import models

# Create your models here.

class ScheduleModel(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    title       = models.CharField('イベント名', max_length=200)
    country     = models.CharField('対象国', max_length=200)
    priority    = models.IntegerField('イベントの重要性', default=0)
    target      = models.BooleanField('対象の可否', default=True)
    # available   = models.BooleanField(default=True)
    presentation_time   = models.DateTimeField('イベント時刻')

class ProcessModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    pid         = models.IntegerField('プロセスID')
    status      = models.BooleanField('状態', default=True)
    created     = models.DateTimeField('生成時刻', auto_now_add=True)
    endtime     = models.DateTimeField('終了時刻', blank=True, null=True)

# class TransactionModel(models.Model):
#     process     = models.ForeignKey(ProcessModel)
#     created     = models.DateTimeField('生成時間', auto_now_add=True)

class PricesModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    ask         = models.FloatField(default=0)
    bid         = models.FloatField(default=0)
    instrument  = models.CharField(max_length=100, blank=True, null=True)
    time        = models.DateTimeField('対象サーバー時刻', blank=True, null=True)
    begin       = models.DateTimeField('開始時刻')
    end         = models.DateTimeField('終了時刻', blank=True, null=True)
    created     = models.DateTimeField('DB生成時刻', auto_now_add=True)