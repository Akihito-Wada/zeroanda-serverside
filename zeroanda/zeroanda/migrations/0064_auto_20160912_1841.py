# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroanda', '0063_economicindicatormanagementmodel_economicindicatormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economicindicatormodel',
            name='actual',
            field=models.CharField(default=0, max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='economicindicatormodel',
            name='forecast',
            field=models.CharField(default=0, max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='economicindicatormodel',
            name='importance',
            field=models.IntegerField(default=0, choices=[(0, 'LOW'), (1, 'MEDIUM'), (2, 'HIGH')], verbose_name='重要度'),
        ),
        migrations.AlterField(
            model_name='economicindicatormodel',
            name='previous',
            field=models.CharField(default=0, max_length=200, null=True, blank=True),
        ),
    ]
