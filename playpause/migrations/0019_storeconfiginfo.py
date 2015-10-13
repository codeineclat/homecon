# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playpause', '0018_auto_20150926_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storeconfiginfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('xbee_name', models.CharField(max_length=256, default='')),
                ('xbee_number', models.CharField(max_length=256, default='')),
            ],
        ),
    ]
