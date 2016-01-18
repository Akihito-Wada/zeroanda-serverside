# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0020_pricesmodel_elapsed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricesmodel',
            name='elapsed',
            field=models.CharField(null=True, blank=True, verbose_name='経過時間', max_length=10),
        ),
    ]
