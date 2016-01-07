# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0004_auto_20160106_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActualOrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('status', models.IntegerField(default=1, choices=[(1, 'Progress'), (2, 'Finish')])),
                ('time', models.DateTimeField(blank=True, verbose_name='対象サーバー時刻', null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻')),
                ('updated', models.DateTimeField(blank=True, verbose_name='更新時刻', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruments', models.CharField(max_length=30, choices=[('USD_JPY', 'us')])),
                ('units', models.IntegerField(default=1)),
                ('side', models.CharField(max_length=3, choices=[('sell', 'Sell'), ('buy', 'Buy')])),
                ('type', models.CharField(max_length=20, choices=[('limit', 'Limit'), ('stop', 'Stop'), ('marketIfTouched', 'MarketIfTouched'), ('market', 'Market')])),
                ('expirey', models.DateTimeField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('uppperBound', models.FloatField(default=0, verbose_name='成立上限価格')),
                ('lowerBound', models.FloatField(default=0, verbose_name='成立下限価格')),
                ('stopLoss', models.FloatField(default=0)),
                ('takeProfit', models.FloatField(default=0)),
                ('traillingStop', models.FloatField(default=0)),
                ('status', models.BooleanField(default=True, choices=[(True, 'available'), (False, 'disable')])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻')),
                ('updated', models.DateTimeField(blank=True, verbose_name='更新時刻', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='イベントの重要性', choices=[(1, 'Lowest'), (2, 'Low'), (3, 'Intermediate'), (4, 'High'), (5, 'Highest')]),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='schedule',
            field=models.ForeignKey(to='zeroanda.ScheduleModel'),
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
