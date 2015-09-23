# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0016_auto_20150924_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetlastSong',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('song_name', models.CharField(default='', max_length=256)),
                ('song_id', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
