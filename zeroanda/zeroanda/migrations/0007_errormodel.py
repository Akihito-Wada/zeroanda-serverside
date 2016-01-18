# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0006_auto_20160113_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('messag', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録時刻')),
            ],
        ),
    ]
