# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0047_transactionmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='presentation_time',
            field=models.DateTimeField(verbose_name='実行予定時刻', null=True),
        ),
    ]
