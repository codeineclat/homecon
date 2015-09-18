# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0007_auto_20150919_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='log_at',
            field=models.DateTimeField(default=None, blank=True),
        ),
    ]
