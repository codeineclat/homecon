# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_recent_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recent_request',
            name='request_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
