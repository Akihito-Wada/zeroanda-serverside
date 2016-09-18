# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0064_auto_20160912_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulemodel',
            name='instrument',
            field=models.CharField(max_length=200, default=0, verbose_name='貨幣', choices=[('USD_JPY', 'us_jp'), ('EUR_JPY', 'eu_jp'), ('EUR_USD', 'eu_us'), ('EUR_CAD', 'eu_ca')]),
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='country',
            field=models.CharField(max_length=200, default=4, verbose_name='対象国', choices=[('0', 'Australia'), ('1', 'Canada'), ('2', 'England'), ('3', 'European Union'), ('4', 'Japan'), ('5', 'New Zealand'), ('6', 'Switzerland'), ('7', 'United States'), ('8', "People's Republic of China")]),
        ),
    ]
