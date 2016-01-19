# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0029_auto_20160119_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmodel',
            name='schedule',
        ),
    ]
