from django.db import models
from zeroanda.constant import ORDER_STATUS, PRIORITY, SIDE, ACTUAL_ORDER_STATUS, INSTRUMENTS, TYPE, SCHEDULE_STATUS

# Create your models here.

class ScheduleModel(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    title       = models.CharField('イベント名', max_length=200)
    country     = models.CharField('対象国', max_length=200)
    priority    = models.IntegerField('イベントの重要性', choices=PRIORITY, default=PRIORITY[2][0])
    target      = models.BooleanField('対象の可否', choices=SCHEDULE_STATUS, default=SCHEDULE_STATUS[0][0])
    presentation_time   = models.DateTimeField('イベント時刻')

class ProcessModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    pid         = models.IntegerField('プロセスID')
    status      = models.BooleanField('状態', default=True)
    created     = models.DateTimeField('生成時刻', auto_now_add=True)
    endtime     = models.DateTimeField('終了時刻', blank=True, null=True)

class PricesModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    ask         = models.FloatField(default=0)
    bid         = models.FloatField(default=0)
    instrument  = models.CharField(max_length=100, blank=True, null=True)
    time        = models.DateTimeField('対象サーバー時刻', blank=True, null=True)
    begin       = models.DateTimeField('開始時刻')
    end         = models.DateTimeField('終了時刻', blank=True, null=True)
    created     = models.DateTimeField('DB生成時刻', auto_now_add=True)

class OrderModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    instruments = models.CharField(max_length=30, choices=INSTRUMENTS)
    units       = models.IntegerField(default=1)
    side        = models.CharField(max_length=3, choices=SIDE)
    type        = models.CharField(max_length=20, choices=TYPE)
    expirey     = models.DateTimeField(blank=True, null=True)
    price       = models.FloatField()
    uppperBound = models.FloatField("成立上限価格", default=0)
    lowerBound  = models.FloatField("成立下限価格", default=0)
    stopLoss    = models.FloatField(default=0)
    takeProfit  = models.FloatField(default=0)
    traillingStop   = models.FloatField(default=0)
    status      = models.BooleanField(choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)

class ActualOrderModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    order       = models.OneToOneField(OrderModel)
    instruments = models.CharField(max_length=200)
    units       = models.IntegerField(default=1)
    side        = models.CharField(max_length=200)
    type        = models.CharField(max_length=200)
    expirey     = models.DateTimeField(blank=True, null=True)
    price       = models.FloatField()
    uppperBound = models.FloatField("成立上限価格", default=0)
    lowerBound  = models.FloatField("成立下限価格", default=0)
    stopLoss    = models.FloatField(default=0)
    takeProfit  = models.FloatField(default=0)
    traillingStop   = models.FloatField(default=0)
    status      = models.IntegerField(choices=ACTUAL_ORDER_STATUS, default=ACTUAL_ORDER_STATUS[0][0])
    time        = models.DateTimeField('対象サーバー時刻', blank=True, null=True)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)

class AccountModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    account_id  = models.IntegerField()
    margin_rate = models.FloatField()
    account_currency    = models.CharField(max_length=10)
    account_name    = models.CharField(max_length=10)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)