# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0030_remove_accountmodel_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actualordermodel',
            old_name='expirey',
            new_name='expiry',
        ),
        migrations.RenameField(
            model_name='actualordermodel',
            old_name='traillingStop',
            new_name='trailingStop',
        ),
        migrations.RemoveField(
            model_name='actualordermodel',
            name='type',
        ),
        migrations.AddField(
            model_name='actualordermodel',
            name='actual_order_id',
            field=models.IntegerField(default=0),
        ),
    ]
