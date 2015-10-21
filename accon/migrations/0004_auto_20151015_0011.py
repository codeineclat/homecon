# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accon', '0003_acdetails_current_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aclog',
            name='log_cmd',
        ),
        migrations.RemoveField(
            model_name='aclog',
            name='log_function',
        ),
        migrations.AddField(
            model_name='aclog',
            name='log_deviced',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='aclog',
            name='log_speed',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AlterField(
            model_name='aclog',
            name='log_value',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
