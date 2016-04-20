# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0058_auto_20160420_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='lowerBound',
            field=models.FloatField(default=0, verbose_name='成立下限価格'),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='side',
            field=models.CharField(max_length=200, blank=True, null=True, choices=[('sell', 'Sell'), ('buy', 'Buy')]),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='stopLoss',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='upperBound',
            field=models.FloatField(default=0, verbose_name='成立上限価格'),
        ),
    ]
