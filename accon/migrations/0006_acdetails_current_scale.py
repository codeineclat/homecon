# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accon', '0005_auto_20151015_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='acdetails',
            name='current_scale',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
