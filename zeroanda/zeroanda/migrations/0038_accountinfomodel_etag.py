# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0037_accountmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinfomodel',
            name='etag',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
