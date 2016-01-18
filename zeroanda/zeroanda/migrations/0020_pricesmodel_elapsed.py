# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0019_pricesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricesmodel',
            name='elapsed',
            field=models.FloatField(verbose_name='経過時間', null=True, blank=True),
        ),
    ]
