# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0004_log_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='log_appid',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
