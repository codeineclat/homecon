# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recent_Request',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('request_at', models.DateTimeField(blank=True)),
                ('request_packet', models.TextField(default='')),
                ('request_siliconid', models.CharField(max_length=16)),
                ('served_at', models.DateTimeField(blank=True)),
                ('sucess_at', models.DateTimeField(blank=True)),
                ('request_status', models.BooleanField(default=0)),
            ],
        ),
    ]
