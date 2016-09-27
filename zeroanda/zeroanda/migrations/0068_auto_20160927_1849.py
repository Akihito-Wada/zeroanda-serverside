# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0067_auto_20160927_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='order_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
