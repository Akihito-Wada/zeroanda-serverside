# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0032_auto_20160120_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualordermodel',
            name='error_code',
            field=models.IntegerField(choices=[(0, 'None'), (11, 'Order not found')], default=0),
        ),
        migrations.AlterField(
            model_name='actualordermodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'Progress'), (2, 'Finish')], default=1),
        ),
    ]
