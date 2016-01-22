# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0036_accountmodel_etag'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='status',
            field=models.BooleanField(choices=[(True, 'available'), (False, 'disable')], default=True),
        ),
    ]
