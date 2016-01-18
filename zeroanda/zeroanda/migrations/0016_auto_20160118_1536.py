# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0015_pricesmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricesmodel',
            name='schedule',
        ),
        migrations.DeleteModel(
            name='PricesModel',
        ),
    ]
