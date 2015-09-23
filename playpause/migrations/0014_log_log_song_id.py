# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0013_log_log_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='log_song_id',
            field=models.IntegerField(null=True, default=0),
        ),
    ]
