# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0026_auto_20160119_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='side',
            field=models.CharField(choices=[('sell', 'Sell'), ('buy', 'Buy')], max_length=4),
        ),
    ]
