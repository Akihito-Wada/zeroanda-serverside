# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0069_transactionmodel_actual_trade_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactionmodel',
            old_name='actual_order_id',
            new_name='transaction_id',
        ),
    ]
