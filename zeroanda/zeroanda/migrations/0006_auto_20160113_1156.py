# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0005_auto_20160107_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('margin_rate', models.FloatField()),
                ('account_currency', models.CharField(max_length=10)),
                ('account_name', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='更新時刻')),
            ],
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='instruments',
            field=models.CharField(max_length=30, choices=[('USD_JPY', 'us_jp'), ('EUR_JPY', 'eu_jp'), ('EUR_USD', 'eu_us'), ('EUR_CAD', 'eu_ca')]),
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='priority',
            field=models.IntegerField(default=3, verbose_name='イベントの重要性', choices=[(1, 'Lowest'), (2, 'Low'), (3, 'Intermediate'), (4, 'High'), (5, 'Highest')]),
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='target',
            field=models.BooleanField(default=True, verbose_name='対象の可否', choices=[(True, '有効'), (False, '無効')]),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='schedule',
            field=models.ForeignKey(to='zeroanda.ScheduleModel'),
        ),
    ]
