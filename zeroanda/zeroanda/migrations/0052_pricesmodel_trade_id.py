# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0051_ordermodel_trade_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricesmodel',
            name='trade_id',
            field=models.IntegerField(default=0),
        ),
    ]
