# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0033_auto_20160120_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='expirey',
            new_name='expiry',
        ),
        migrations.AlterField(
            model_name='actualordermodel',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, 'Progress'), (2, 'Finish'), (3, 'Cancel')]),
        ),
    ]
