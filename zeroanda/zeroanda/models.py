from django.db import models
from zeroanda.constant import ORDER_STATUS, PRIORITY, SIDE, ACTUAL_ORDER_STATUS, INSTRUMENTS, TYPE, SCHEDULE_AVAILABLE, SCHEDULE_STATUS, COUNTRY_LIST, ERROR_CODE, ACCOUNT_STATUS, TRANSACTION_REASON, TRANSACTION_TYPE

class ScheduleModel(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    title       = models.CharField('イベント名', max_length=200)
    country     = models.CharField('対象国', max_length=200, choices=COUNTRY_LIST)
    priority    = models.IntegerField('イベントの重要性', choices=PRIORITY, default=PRIORITY[2][0])
    target      = models.BooleanField('対象の可否', choices=SCHEDULE_AVAILABLE, default=SCHEDULE_AVAILABLE[0][0])
    status      = models.IntegerField('状況', choices=SCHEDULE_STATUS, default=SCHEDULE_STATUS[0][0])
    presentation_time   = models.DateTimeField('イベント時刻')
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)

    # def get_instrument(self):
    #     return

class ProcessModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel)
    pid         = models.IntegerField('プロセスID')
    status      = models.BooleanField('状態', default=True)
    created     = models.DateTimeField('生成時刻', auto_now_add=True)
    endtime     = models.DateTimeField('終了時刻', blank=True, null=True)

class PricesModel(models.Model):
    trade_id    = models.IntegerField(default=0)
    ask         = models.FloatField(default=0)
    bid         = models.FloatField(default=0)
    instrument  = models.CharField(max_length=100, blank=True, null=True)
    etag        = models.CharField(max_length=100, null=True, blank=True)
    time        = models.DateTimeField('対象サーバー時刻', blank=True, null=True)
    # begin       = models.DateTimeField('開始時刻')
    # end         = models.DateTimeField('終了時刻', blank=True, null=True)
    # elapsed     = models.CharField('経過時間', blank=True, null=True, max_length=20)
    created     = models.DateTimeField('DB生成時刻', auto_now_add=True)

class OrderModel(models.Model):
    trade_id    = models.IntegerField(default=0)
    schedule    = models.ForeignKey(ScheduleModel, blank=True, null=True)
    instruments = models.CharField(max_length=30, choices=INSTRUMENTS)
    units       = models.IntegerField(default=0)
    side        = models.CharField(max_length=4, choices=SIDE)
    type        = models.CharField(max_length=20, choices=TYPE)
    expiry      = models.DateTimeField(blank=True, null=True)
    price       = models.FloatField(default=1, blank=True, null=True)
    upperBound = models.FloatField("成立上限価格", blank=True, null=True)
    lowerBound  = models.FloatField("成立下限価格", blank=True, null=True)
    stopLoss    = models.FloatField(default=0, blank=True, null=True)
    takeProfit  = models.FloatField(default=0, blank=True, null=True)
    traillingStop   = models.FloatField(default=0, blank=True, null=True)
    status      = models.IntegerField(choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)

class ActualOrderModel(models.Model):
    trade_id    = models.IntegerField(default=0)
    schedule    = models.ForeignKey(ScheduleModel, blank=True, null=True)
    order       = models.OneToOneField(OrderModel, related_name='actual_model')
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

class TransactionModel(models.Model):
    actual_order_id= models.BigIntegerField(default=0)
    accountBalance  = models.FloatField(default=0)
    trade_id    = models.IntegerField(default=0)
    schedule    = models.ForeignKey(ScheduleModel, blank=True, null=True)
    actual_order_model = models.ForeignKey(ActualOrderModel, blank=True, null=True, related_name='transaction_model')
    instruments = models.CharField(max_length=200, blank=True, null=True)
    interest    = models.FloatField(default=0)
    order_id    = models.IntegerField(default=0)
    pl          = models.FloatField(default=0)
    units       = models.IntegerField(default=1)
    side        = models.CharField(max_length=200, choices=SIDE, blank=True, null=True)
    expiry      = models.DateTimeField(blank=True, null=True)
    price       = models.FloatField(default=0, blank=True, null=True)
    upperBound  = models.FloatField("成立上限価格", default=0)
    lowerBound  = models.FloatField("成立下限価格", default=0)
    stopLoss    = models.FloatField(default=0)
    type        = models.IntegerField(choices=TRANSACTION_TYPE, default=TRANSACTION_TYPE[0][0])
    reason      = models.IntegerField(choices=TRANSACTION_REASON, default=TRANSACTION_REASON[0][0])
    time        = models.DateTimeField('対象サーバー時刻', blank=True, null=True)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)

class AccountModel(models.Model):
    # schedule    = models.ForeignKey(ScheduleModel)
    account_id  = models.IntegerField()
    account_currency    = models.CharField(max_length=10)
    account_name    = models.CharField(max_length=10)
    margin_rate = models.FloatField(default=0)
    etag        = models.CharField(max_length=100, null=True, blank=True)
    status      = models.BooleanField(default=ACCOUNT_STATUS[0][0], choices=ACCOUNT_STATUS)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)

class AccountInfoModel(models.Model):
    # schedule    = models.ForeignKey(ScheduleModel)
    account_model     = models.ForeignKey(AccountModel)
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
    etag        = models.CharField(max_length=100, null=True, blank=True)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)
    updated     = models.DateTimeField('更新時刻', null=True, blank=True)


class ErrorModel(models.Model):
    status_code = models.IntegerField(default=0)
    code        = models.IntegerField()
    message      = models.CharField(max_length=200)
    info        = models.CharField(max_length=200)
    created     = models.DateTimeField('登録時刻', auto_now_add=True)

class TradeModel(models.Model):
    schedule    = models.ForeignKey(ScheduleModel, blank=True, null=True)
    presentation_time   = models.DateTimeField('イベント時刻')
    created     = models.DateTimeField('登録時刻', auto_now_add=True)

class TradeTransactionModel(models.Model):
    trade_model     = models.ForeignKey(TradeModel)
    transaction_name= models.CharField(max_length=200)
    created     = models.DateTimeField('登録時刻', auto_now_add=True, null=True)
    presentation_time= models.DateTimeField('実行予定時刻', null=True)
    excute_time= models.DateTimeField('実行時刻', null=True)