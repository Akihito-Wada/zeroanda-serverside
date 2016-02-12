# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0041_auto_20160126_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='lowerBound',
            field=models.FloatField(null=True, blank=True, verbose_name='成立下限価格'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='price',
            field=models.FloatField(null=True, blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='stopLoss',
            field=models.FloatField(null=True, blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='takeProfit',
            field=models.FloatField(null=True, blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='traillingStop',
            field=models.FloatField(null=True, blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='upperBound',
            field=models.FloatField(null=True, blank=True, verbose_name='成立上限価格'),
        ),
    ]
