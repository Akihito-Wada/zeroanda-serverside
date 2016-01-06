# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0002_auto_20160106_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processmodel',
            name='schedule',
            field=models.ForeignKey(to='zeroanda.ScheduleModel'),
        ),
    ]
