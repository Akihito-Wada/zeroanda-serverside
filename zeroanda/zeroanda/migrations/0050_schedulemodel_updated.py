# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0049_schedulemodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulemodel',
            name='updated',
            field=models.DateTimeField(verbose_name='更新時刻', null=True, blank=True),
        ),
    ]
