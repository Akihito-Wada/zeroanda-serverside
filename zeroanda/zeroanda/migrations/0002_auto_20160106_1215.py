# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processmodel',
            name='endtime',
            field=models.DateTimeField(verbose_name='終了時間', null=True, blank=True),
        ),
    ]
