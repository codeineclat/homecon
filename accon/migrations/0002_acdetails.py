# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACDetails',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('device_name', models.CharField(default='0', max_length=20)),
                ('device_info', models.CharField(default='', max_length=256)),
                ('device_id', models.IntegerField(null=True, default=0)),
                ('device_img_on', models.CharField(default='', max_length=256)),
                ('device_img_off', models.CharField(default='', max_length=256)),
                ('device_place', models.IntegerField(null=True, default=0)),
            ],
        ),
    ]
