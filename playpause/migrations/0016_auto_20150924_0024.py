# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0015_errorlog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='errorlog',
            old_name='error_time',
            new_name='error_at',
        ),
    ]
