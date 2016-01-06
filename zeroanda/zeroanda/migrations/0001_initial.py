# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pid', models.IntegerField(verbose_name='プロセスID')),
                ('status', models.BooleanField(default=True, verbose_name='状態')),
                ('created', models.DateTimeField(verbose_name='生成時間', auto_now_add=True)),
                ('endtime', models.DateTimeField(default=None, verbose_name='終了時間')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, verbose_name='イベント名')),
                ('country', models.CharField(max_length=200, verbose_name='対象国')),
                ('priority', models.IntegerField(default=0, verbose_name='イベントの重要性')),
                ('target', models.BooleanField(default=True, verbose_name='対象の可否')),
                ('presentation_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='processmodel',
            name='schedule',
            field=models.OneToOneField(to='zeroanda.ScheduleModel'),
        ),
    ]
