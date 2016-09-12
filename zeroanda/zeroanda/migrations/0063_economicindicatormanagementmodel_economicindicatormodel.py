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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('origin', models.CharField(max_length=200, verbose_name='取得先')),
                ('unique_id', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200, verbose_name='取得URL')),
                ('filename', models.CharField(max_length=200, verbose_name='取得ファイル')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, verbose_name='更新時刻', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EconomicIndicatorModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('raw_date', models.CharField(max_length=200, blank=True, verbose_name='日付', null=True)),
                ('raw_time', models.CharField(max_length=200, blank=True, verbose_name='時刻', null=True)),
                ('time_zone', models.CharField(max_length=200, verbose_name='タイムゾーン')),
                ('currency', models.CharField(max_length=200, verbose_name='通貨')),
                ('event', models.CharField(max_length=200, verbose_name='イベント')),
                ('importance', models.IntegerField(verbose_name='重要度', choices=[(0, 'LOW'), (1, 'MIDDLE'), (2, 'HIGH')], default=0)),
                ('actual', models.FloatField(default=0)),
                ('forecast', models.FloatField(default=0)),
                ('previous', models.FloatField(default=0)),
                ('date', models.DateTimeField(null=True, verbose_name='更新時刻', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='生成時刻')),
                ('updated', models.DateTimeField(null=True, verbose_name='更新時刻', blank=True)),
                ('management_model', models.ForeignKey(to='zeroanda.EconomicIndicatorManagementModel')),
            ],
        ),
    ]
