# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0065_auto_20160919_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='actualordermodel',
            name='order',
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='instrument',
            field=models.CharField(max_length=200, choices=[('USD_JPY', 'USD_JPY'), ('EUR_JPY', 'EUR_JPY'), ('EUR_USD', 'EUR_USD'), ('EUR_CAD', 'EUR_CAD')], verbose_name='貨幣', default=0),
        ),
        migrations.DeleteModel(
            name='OrderModel',
        ),
    ]
