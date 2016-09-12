# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0062_auto_20160906_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicIndicatorManagementModel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('origin', models.CharField(verbose_name='取得先', max_length=200)),
                ('url', models.CharField(verbose_name='取得URL', max_length=200)),
                ('filename', models.CharField(verbose_name='取得ファイル', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='更新時刻', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EconomicIndicatorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('raw_date', models.CharField(verbose_name='日付', blank=True, max_length=200, null=True)),
                ('raw_time', models.CharField(verbose_name='時刻', blank=True, max_length=200, null=True)),
                ('timezone', models.IntegerField(default=2, choices=[(0, 'Lowest'), (1, 'Low'), (2, 'Intermediate'), (3, 'High'), (4, 'Highest')], verbose_name='タイムゾーン')),
                ('currency', models.BooleanField(verbose_name='通貨', choices=[(True, '有効'), (False, '無効')], default=True)),
                ('event', models.IntegerField(verbose_name='イベント')),
                ('importance', models.DateTimeField(default=0, choices=[(0, 'LOW'), (1, 'MIDDLE'), (2, 'HIGH')], verbose_name='重要度')),
                ('actual', models.FloatField(default=0)),
                ('forecast', models.FloatField(default=0)),
                ('previous', models.FloatField(default=0)),
                ('date', models.DateTimeField(verbose_name='更新時刻', blank=True, null=True)),
                ('created', models.DateTimeField(verbose_name='生成時刻', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='更新時刻', blank=True, null=True)),
                ('schedule', models.ForeignKey(to='zeroanda.EconomicIndicatorManagementModel')),
            ],
        ),
    ]
