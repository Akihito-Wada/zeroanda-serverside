# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0024_auto_20160119_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actualordermodel',
            name='schedule',
        ),
        migrations.DeleteModel(
            name='ActualOrderModel',
        ),
    ]
