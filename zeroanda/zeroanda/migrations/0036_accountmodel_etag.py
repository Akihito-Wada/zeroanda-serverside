# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0035_auto_20160121_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='etag',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
