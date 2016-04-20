# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0053_actualordermodel_trade_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeTransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('transaction_name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻', null=True)),
                ('presentation_time', models.DateTimeField(verbose_name='実行予定時刻', null=True)),
                ('excute_time', models.DateTimeField(verbose_name='実行時刻', null=True)),
                ('trade_model', models.ForeignKey(to='zeroanda.TradeModel')),
            ],
        ),
        migrations.RemoveField(
            model_name='transactionmodel',
            name='trade_model',
        ),
        migrations.DeleteModel(
            name='TransactionModel',
        ),
    ]
