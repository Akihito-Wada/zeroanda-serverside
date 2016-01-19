# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0022_auto_20160118_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualordermodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'Progress'), (2, 'Finish'), (3, 'Fail')], default=1),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.IntegerField(choices=[(True, 'available'), (False, 'disable')], default=True),
        ),
    ]
