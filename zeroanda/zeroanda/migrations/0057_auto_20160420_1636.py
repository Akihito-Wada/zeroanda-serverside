# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0056_auto_20160420_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='actual_order_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
