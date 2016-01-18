# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0013_remove_pricesmodel_elapsed'),
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
