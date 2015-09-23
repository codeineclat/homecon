# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0012_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='log_song',
            field=models.CharField(default='', max_length=256),
        ),
    ]
