# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0042_auto_20160212_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='schedule',
            field=models.ForeignKey(null=True, to='zeroanda.ScheduleModel', blank=True),
        ),
    ]
