# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0003_auto_20160106_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.FloatField(default=0)),
                ('bid', models.FloatField(default=0)),
                ('time', models.DateTimeField(verbose_name='対象サーバー時刻', null=True, blank=True)),
                ('instrument', models.CharField(max_length=100, null=True, blank=True)),
                ('begin', models.DateTimeField(verbose_name='開始時刻')),
                ('end', models.DateTimeField(verbose_name='終了時刻', null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='DB生成時刻')),
            ],
        ),
        migrations.AlterField(
            model_name='processmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='生成時刻'),
        ),
        migrations.AlterField(
            model_name='processmodel',
            name='endtime',
            field=models.DateTimeField(verbose_name='終了時刻', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='presentation_time',
            field=models.DateTimeField(verbose_name='イベント時刻'),
        ),
        migrations.AddField(
            model_name='pricesmodel',
            name='schedule',
            field=models.ForeignKey(to='zeroanda.ScheduleModel'),
        ),
    ]
