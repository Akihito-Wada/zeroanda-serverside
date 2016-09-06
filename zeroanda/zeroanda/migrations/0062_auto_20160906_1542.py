# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0061_auto_20160809_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errormodel',
            name='code',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='errormodel',
            name='info',
            field=models.CharField(default=None, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='errormodel',
            name='message',
            field=models.CharField(default=None, blank=True, max_length=200),
        ),
    ]
