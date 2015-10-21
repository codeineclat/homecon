# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accon', '0004_auto_20151015_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aclog',
            old_name='log_deviced',
            new_name='log_deviceid',
        ),
    ]
