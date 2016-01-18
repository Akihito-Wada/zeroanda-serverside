# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0018_auto_20160118_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricesModel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ask', models.FloatField(default=0)),
                ('bid', models.FloatField(default=0)),
                ('instrument', models.CharField(max_length=100, blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='対象サーバー時刻')),
                ('begin', models.DateTimeField(verbose_name='開始時刻')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='終了時刻')),
                ('created', models.DateTimeField(verbose_name='DB生成時刻', auto_now_add=True)),
                ('schedule', models.ForeignKey(to='zeroanda.ScheduleModel')),
            ],
        ),
    ]
