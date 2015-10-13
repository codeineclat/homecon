# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20150919_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Errorlog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('error_name', models.CharField(max_length=1000, default='')),
                ('error_at', models.DateTimeField(default=None, blank=True)),
            ],
        ),
    ]
