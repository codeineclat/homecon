# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0008_auto_20150919_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('log_id', models.IntegerField(null=True)),
                ('siliconid', models.CharField(max_length=20, default='')),
                ('fail_at', models.DateTimeField(blank=True, default=None)),
            ],
        ),
    ]
