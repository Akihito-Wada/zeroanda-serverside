# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0039_pricesmodel_etag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricesmodel',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='pricesmodel',
            name='elapsed',
        ),
        migrations.RemoveField(
            model_name='pricesmodel',
            name='end',
        ),
        migrations.RemoveField(
            model_name='pricesmodel',
            name='schedule',
        ),
    ]
