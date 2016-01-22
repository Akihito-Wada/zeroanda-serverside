# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0034_auto_20160120_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('account_id', models.IntegerField()),
                ('account_currency', models.CharField(max_length=10)),
                ('account_name', models.CharField(max_length=10)),
                ('balance', models.IntegerField(default=0)),
                ('margin_rate', models.FloatField(default=0)),
                ('margin_used', models.FloatField(default=0)),
                ('margin_avail', models.IntegerField(default=0)),
                ('open_orders', models.IntegerField(default=0)),
                ('open_trades', models.IntegerField(default=0)),
                ('unrealized_pl', models.FloatField(default=0)),
                ('realized_pl', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻')),
                ('updated', models.DateTimeField(verbose_name='更新時刻', blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='margin_avail',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='margin_used',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='open_orders',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='open_trades',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='realized_pl',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='unrealized_pl',
        ),
        migrations.AddField(
            model_name='accountinfomodel',
            name='account_model',
            field=models.ForeignKey(to='zeroanda.AccountModel'),
        ),
    ]
