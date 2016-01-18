# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0008_auto_20160118_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='margin_avail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='margin_used',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='open_orders',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='open_trades',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='realized_pl',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='unrealized_pl',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='margin_rate',
            field=models.FloatField(default=0),
        ),
    ]
