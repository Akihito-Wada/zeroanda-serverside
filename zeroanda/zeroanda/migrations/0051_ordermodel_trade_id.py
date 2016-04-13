# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0050_schedulemodel_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='trade_id',
            field=models.IntegerField(default=0),
        ),
    ]
