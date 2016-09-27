# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0066_auto_20160927_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactionmodel',
            old_name='lowerBound',
            new_name='lower_bound',
        ),
        migrations.RenameField(
            model_name='transactionmodel',
            old_name='stopLoss',
            new_name='stop_loss',
        ),
        migrations.RenameField(
            model_name='transactionmodel',
            old_name='upperBound',
            new_name='upper_bound',
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='account_balance',
            field=models.FloatField(default=0, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='take_profit_price',
            field=models.FloatField(default=0, blank=True, null=True),
        ),
    ]
