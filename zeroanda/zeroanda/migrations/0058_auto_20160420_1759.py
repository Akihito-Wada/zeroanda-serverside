# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0057_auto_20160420_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='instruments',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='lowerBound',
            field=models.FloatField(verbose_name='成立下限価格', default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='price',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='stopLoss',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='upperBound',
            field=models.FloatField(verbose_name='成立上限価格', default=0, null=True, blank=True),
        ),
    ]
