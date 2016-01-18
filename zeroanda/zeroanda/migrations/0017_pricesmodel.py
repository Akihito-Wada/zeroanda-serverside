# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0016_auto_20160118_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ask', models.FloatField(default=0)),
                ('bid', models.FloatField(default=0)),
                ('instrument', models.CharField(null=True, max_length=100, blank=True)),
                ('time', models.DateTimeField(null=True, blank=True, verbose_name='対象サーバー時刻')),
                ('begin', models.DateTimeField(verbose_name='開始時刻')),
                ('end', models.DateTimeField(null=True, blank=True, verbose_name='終了時刻')),
                ('elapsed', models.FloatField(null=True, blank=True, verbose_name='経過時間')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='DB生成時刻')),
                ('schedule', models.ForeignKey(to='zeroanda.ScheduleModel')),
            ],
        ),
    ]
