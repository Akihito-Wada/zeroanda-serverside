# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0046_auto_20160404_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='created',
            field=models.DateTimeField(null=True, verbose_name='登録時刻', auto_now_add=True),
        ),
    ]
