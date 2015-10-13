# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_errorlog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Errorlog',
            new_name='Serrorlog',
        ),
    ]
