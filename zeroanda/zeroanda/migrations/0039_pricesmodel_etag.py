# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0038_accountinfomodel_etag'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricesmodel',
            name='etag',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
