from django.db import models
from zeroanda.constant import ORDER_STATUS, PRIORITY, SIDE, ACTUAL_ORDER_STATUS, INSTRUMENTS, TYPE, SCHEDULE_STATUS, COUNTRY_LIST, ERROR_CODE

class ScheduleModel(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    title       = models.CharField('イベント名', max_length=200)
    country     = models.CharField('対象国', max_length=200, choices=COUNTRY_LIST)
    priority    = models.IntegerField('イベントの重要性', choices=PRIORITY, default=PRIORITY[2][0])
    target      = models.BooleanField('対象の可否', choices=SCHEDULE_STATUS, default=SCHEDULE_STATUS[0][0])
    presentation_time   = models.DateTimeField('イベント時刻')

    def get_instrument(self):
        return

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
    elapsed     = models.CharField('経過時間', blank=True, null=True, max_length=20)
    created     = models.DateTimeField('DB生成時刻', auto_now_add=True)

class OrderModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    instruments = models.CharField(max_length=30, choices=INSTRUMENTS)
    units       = models.IntegerField(default=1)
    side        = models.CharField(max_length=4, choices=SIDE)
    type        = models.CharField(max_length=20, choices=TYPE)
    expiry      = models.DateTimeField(blank=True, null=True)
    price       = models.FloatField(default=1)
    upperBound = models.FloatField("成立上限価格", default=0)
    lowerBound  = models.FloatField("成立下限価格", default=0)
    stopLoss    = models.FloatField(default=0)
    takeProfit  = models.FloatField(default=0)
    traillingStop   = models.FloatField(default=0)
    status      = models.IntegerField(choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)

class ActualOrderModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    order       = models.OneToOneField(OrderModel)
    actual_order_id    = models.BigIntegerField(default=0)
    instruments = models.CharField(max_length=200)
    units       = models.IntegerField(default=1)
    side        = models.CharField(max_length=200)
    expiry      = models.DateTimeField(blank=True, null=True)
    price       = models.FloatField()
    upperBound = models.FloatField("成立上限価格", default=0)
    lowerBound  = models.FloatField("成立下限価格", default=0)
    stopLoss    = models.FloatField(default=0)
    takeProfit  = models.FloatField(default=0)
    trailingStop   = models.FloatField(default=0)
    status      = models.IntegerField(choices=ACTUAL_ORDER_STATUS, default=ACTUAL_ORDER_STATUS[0][0])
    error_code  = models.IntegerField(choices=ERROR_CODE, default=0)
    time        = models.DateTimeField('対象サーバー時刻', blank=True, null=True)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)

class AccountModel(models.Model):
    # schedule    = models.ForeignKey(ScheduleModel)
    account_id  = models.IntegerField()
    account_currency    = models.CharField(max_length=10)
    account_name    = models.CharField(max_length=10)
    balance     = models.IntegerField(default=0)
    margin_rate = models.FloatField(default=0)
    margin_used = models.FloatField(default=0)
    margin_avail= models.IntegerField(default=0)
    open_orders = models.IntegerField(default=0)
    open_trades = models.IntegerField(default=0)
    unrealized_pl= models.FloatField(default=0)
    realized_pl = models.FloatField(default=0)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)

class ErrorModel(models.Model):
    code        = models.IntegerField()
    message      = models.CharField(max_length=200)
    info        = models.CharField(max_length=200)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)