# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0021_auto_20160118_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricesmodel',
            name='elapsed',
            field=models.CharField(null=True, verbose_name='経過時間', blank=True, max_length=20),
        ),
    ]
