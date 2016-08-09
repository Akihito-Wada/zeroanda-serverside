# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0059_auto_20160420_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinfomodel',
            name='account_model',
            field=models.ForeignKey(related_name='account_info', to='zeroanda.AccountModel'),
        ),
        migrations.AlterField(
            model_name='actualordermodel',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Progress'), (1, 'Finish'), (2, 'Cancel')]),
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='priority',
            field=models.IntegerField(default=2, choices=[(0, 'Lowest'), (1, 'Low'), (2, 'Intermediate'), (3, 'High'), (4, 'Highest')], verbose_name='イベントの重要性'),
        ),
    ]
