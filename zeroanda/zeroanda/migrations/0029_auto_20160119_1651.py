# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0028_auto_20160119_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actualordermodel',
            old_name='uppperBound',
            new_name='upperBound',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='uppperBound',
            new_name='upperBound',
        ),
    ]
