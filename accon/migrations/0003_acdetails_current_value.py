# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accon', '0002_acdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='acdetails',
            name='current_value',
            field=models.IntegerField(null=True, default=0),
        ),
    ]
