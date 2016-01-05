# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('priority', models.IntegerField(default=0)),
                ('target', models.BooleanField(default=True)),
                ('presentation_time', models.DateTimeField()),
            ],
        ),
    ]
