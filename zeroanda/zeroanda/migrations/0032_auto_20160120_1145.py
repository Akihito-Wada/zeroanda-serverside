# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0031_auto_20160119_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualordermodel',
            name='actual_order_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
