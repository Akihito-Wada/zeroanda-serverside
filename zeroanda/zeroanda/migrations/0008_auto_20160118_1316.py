# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0007_errormodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='errormodel',
            old_name='messag',
            new_name='message',
        ),
    ]
