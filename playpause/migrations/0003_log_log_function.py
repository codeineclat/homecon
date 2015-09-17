# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0002_log_log_cmd'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='log_function',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
