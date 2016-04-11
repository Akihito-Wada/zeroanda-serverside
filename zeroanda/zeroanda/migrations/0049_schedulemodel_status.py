# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0048_auto_20160404_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulemodel',
            name='status',
            field=models.IntegerField(choices=[(0, 'has been prepared.'), (1, 'has started.'), (2, 'has finished.')], verbose_name='状況', default=0),
        ),
    ]
