# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0045_trademodel_transactionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='excute_time',
            field=models.DateTimeField(verbose_name='実行時刻', null=True),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='presentation_time',
            field=models.DateTimeField(verbose_name='実行予定時刻'),
        ),
    ]
