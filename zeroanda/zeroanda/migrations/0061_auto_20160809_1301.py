# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0060_auto_20160809_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='accountBalance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='interest',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='pl',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accountinfomodel',
            name='account_model',
            field=models.ForeignKey(to='zeroanda.AccountModel'),
        ),
    ]
