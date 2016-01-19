# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0027_auto_20160119_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='price',
            field=models.FloatField(default=1),
        ),
    ]
