# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0005_log_log_appid'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='packet_str',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AddField(
            model_name='log',
            name='sucess_at',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='log',
            name='sucess_status',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='log',
            name='action_at',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='log',
            name='action_taken',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='log',
            name='log_value',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='log',
            name='siliconid',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
