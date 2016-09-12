# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0063_economicindicatormanagementmodel_economicindicatormodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='economicindicatormanagementmodel',
            name='unique_id',
            field=models.IntegerField(default=0),
        ),
    ]
