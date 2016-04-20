# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0055_auto_20160420_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='actual_order_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='actual_order_model',
            field=models.ForeignKey(blank=True, null=True, to='zeroanda.ActualOrderModel', related_name='transaction_model'),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='side',
            field=models.CharField(choices=[('sell', 'Sell'), ('buy', 'Buy')], max_length=200),
        ),
    ]
