# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0064_economicindicatormanagementmodel_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economicindicatormanagementmodel',
            name='unique_id',
            field=models.CharField(max_length=200),
        ),
    ]
