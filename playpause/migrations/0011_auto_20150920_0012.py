# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0010_uploadfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='upload_at',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='user',
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='songfile',
            field=models.FileField(upload_to='songfile/%Y/%m/%d'),
        ),
    ]
