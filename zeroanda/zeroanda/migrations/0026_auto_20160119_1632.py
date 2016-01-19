# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0025_auto_20160119_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActualOrderModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('instruments', models.CharField(max_length=200)),
                ('units', models.IntegerField(default=1)),
                ('side', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('expirey', models.DateTimeField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('uppperBound', models.FloatField(default=0, verbose_name='成立上限価格')),
                ('lowerBound', models.FloatField(default=0, verbose_name='成立下限価格')),
                ('stopLoss', models.FloatField(default=0)),
                ('takeProfit', models.FloatField(default=0)),
                ('traillingStop', models.FloatField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'Progress'), (2, 'Finish'), (3, 'Fail')], default=1)),
                ('time', models.DateTimeField(blank=True, verbose_name='対象サーバー時刻', null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻')),
                ('updated', models.DateTimeField(blank=True, verbose_name='更新時刻', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('instruments', models.CharField(choices=[('USD_JPY', 'us_jp'), ('EUR_JPY', 'eu_jp'), ('EUR_USD', 'eu_us'), ('EUR_CAD', 'eu_ca')], max_length=30)),
                ('units', models.IntegerField(default=1)),
                ('side', models.CharField(choices=[('sell', 'Sell'), ('buy', 'Buy')], max_length=3)),
                ('type', models.CharField(choices=[('limit', 'Limit'), ('stop', 'Stop'), ('marketIfTouched', 'MarketIfTouched'), ('market', 'Market')], max_length=20)),
                ('expirey', models.DateTimeField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('uppperBound', models.FloatField(default=0, verbose_name='成立上限価格')),
                ('lowerBound', models.FloatField(default=0, verbose_name='成立下限価格')),
                ('stopLoss', models.FloatField(default=0)),
                ('takeProfit', models.FloatField(default=0)),
                ('traillingStop', models.FloatField(default=0)),
                ('status', models.IntegerField(choices=[(True, 'available'), (False, 'disable')], default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻')),
                ('updated', models.DateTimeField(blank=True, verbose_name='更新時刻', null=True)),
                ('schedule', models.ForeignKey(to='zeroanda.ScheduleModel')),
            ],
        ),
        migrations.AddField(
            model_name='actualordermodel',
            name='order',
            field=models.OneToOneField(to='zeroanda.OrderModel'),
        ),
        migrations.AddField(
            model_name='actualordermodel',
            name='schedule',
            field=models.ForeignKey(to='zeroanda.ScheduleModel'),
        ),
    ]
