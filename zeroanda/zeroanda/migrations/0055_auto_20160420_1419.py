# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0054_auto_20160419_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('trade_id', models.IntegerField(default=0)),
                ('instruments', models.CharField(max_length=200)),
                ('units', models.IntegerField(default=1)),
                ('side', models.CharField(max_length=200)),
                ('expiry', models.DateTimeField(null=True, blank=True)),
                ('price', models.FloatField()),
                ('upperBound', models.FloatField(verbose_name='成立上限価格', default=0)),
                ('lowerBound', models.FloatField(verbose_name='成立下限価格', default=0)),
                ('stopLoss', models.FloatField(default=0)),
                ('type', models.IntegerField(default=0, choices=[(0, 'UNDEFINED'), (1, 'MARKET_ORDER_CREATE'), (2, 'STOP_ORDER_CREATE'), (3, 'LIMIT_ORDER_CREATE'), (4, 'MARKET_IF_TOUCHED_ORDER_CREATE'), (5, 'ORDER_UPDATE'), (6, 'ORDER_CANCEL'), (7, 'ORDER_FILLED'), (8, 'TRADE_UPDATE'), (9, 'TRADE_CLOSE'), (10, 'MIGRATE_TRADE_OPEN'), (11, 'MIGRATE_TRADE_CLOSE'), (12, 'STOP_LOSS_FILLED'), (13, 'TAKE_PROFIT_FILLED'), (14, 'TRAILING_STOP_FILLED'), (15, 'MARGIN_CALL_ENTER'), (16, 'MARGIN_CALL_EXIT'), (17, 'MARGIN_CLOSEOUT'), (18, 'SET_MARGIN_RATE'), (19, 'TRANSFER_FUNDS'), (20, 'DAILY_INTEREST'), (21, 'FEE')])),
                ('reason', models.IntegerField(default=0, choices=[(0, 'UNDEFINED'), (1, 'CLIENT_REQUEST'), (2, 'TIME_IN_FORCE_EXPIRED'), (3, 'ORDER_FILLED'), (4, 'MIGRATION'), (5, 'INSUFFICIENT_MARGIN'), (6, 'BOUNDS_VIOLATION'), (7, 'UNITS_VIOLATION'), (8, 'STOP_LOSS_VIOLATION'), (9, 'TAKE_PROFIT_VIOLATION'), (10, 'TRAILING_STOP_VIOLATION'), (11, 'MARKET_HALTED'), (12, 'ACCOUNT_NON_TRADABLE'), (13, 'NO_NEW_POSITION_ALLOWED'), (14, 'INSUFFICIENT_LIQUIDITY'), (15, 'ADJUSTMENT'), (16, 'FUNDS'), (17, 'CURRENSEE_MONTHLY'), (18, 'CURRENSEE_PERFORMANCE')])),
                ('time', models.DateTimeField(null=True, verbose_name='対象サーバー時刻', blank=True)),
                ('created', models.DateTimeField(verbose_name='登録時刻', auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='actualordermodel',
            name='order',
            field=models.OneToOneField(to='zeroanda.OrderModel', related_name='actual_model'),
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='actual_order_model',
            field=models.ForeignKey(blank=True, to='zeroanda.ActualOrderModel', null=True),
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='schedule',
            field=models.ForeignKey(blank=True, to='zeroanda.ScheduleModel', null=True),
        ),
    ]
