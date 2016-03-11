# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0043_auto_20160212_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualordermodel',
            name='schedule',
            field=models.ForeignKey(null=True, blank=True, to='zeroanda.ScheduleModel'),
        ),
    ]
