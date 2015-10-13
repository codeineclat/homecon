# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0017_getlastsong'),
    ]

    operations = [
        migrations.RenameField(
            model_name='errorlog',
            old_name='eroor_name',
            new_name='error_name',
        ),
    ]
