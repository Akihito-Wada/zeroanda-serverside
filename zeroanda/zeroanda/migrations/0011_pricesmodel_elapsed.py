# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0010_auto_20160118_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricesmodel',
            name='elapsed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='経過時間'),
        ),
    ]
