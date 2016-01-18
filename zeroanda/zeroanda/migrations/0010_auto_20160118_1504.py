# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0009_auto_20160118_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulemodel',
            name='country',
            field=models.CharField(max_length=200, verbose_name='対象国', choices=[('USD_JPY', 'US')]),
        ),
    ]
