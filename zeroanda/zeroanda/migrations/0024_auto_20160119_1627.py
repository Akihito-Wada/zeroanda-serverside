# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0023_auto_20160119_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='actualordermodel',
            name='order',
        ),
        migrations.DeleteModel(
            name='OrderModel',
        ),
    ]
