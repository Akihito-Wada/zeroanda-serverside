# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0044_auto_20160311_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('presentation_time', models.DateTimeField(verbose_name='イベント時刻')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻')),
                ('schedule', models.ForeignKey(null=True, blank=True, to='zeroanda.ScheduleModel')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('transaction_name', models.CharField(max_length=200)),
                ('presentation_time', models.DateTimeField(auto_now_add=True, verbose_name='実行予定時刻')),
                ('excute_time', models.DateTimeField(auto_now_add=True, verbose_name='実行時刻')),
                ('trade_model', models.ForeignKey(to='zeroanda.TradeModel')),
            ],
        ),
    ]
