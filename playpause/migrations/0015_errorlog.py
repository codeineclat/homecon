# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0014_log_log_song_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Errorlog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('eroor_name', models.CharField(max_length=1000, default='')),
                ('error_time', models.DateTimeField(default=None, blank=True)),
            ],
        ),
    ]
