# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0040_auto_20160126_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='errormodel',
            name='status_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='units',
            field=models.IntegerField(default=0),
        ),
    ]
