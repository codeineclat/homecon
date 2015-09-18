# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0006_auto_20150911_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('log_id', models.IntegerField(null=True)),
                ('siliconid', models.CharField(max_length=20, default='')),
                ('action_at', models.DateTimeField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Sucess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('log_id', models.IntegerField(null=True)),
                ('siliconid', models.CharField(max_length=20, default='')),
                ('sucess_status', models.BooleanField(default=0)),
                ('sucess_at', models.DateTimeField(blank=True, default=None)),
                ('response_str', models.CharField(max_length=256, default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='log',
            name='action_at',
        ),
        migrations.RemoveField(
            model_name='log',
            name='sucess_at',
        ),
        migrations.RemoveField(
            model_name='log',
            name='sucess_status',
        ),
    ]
