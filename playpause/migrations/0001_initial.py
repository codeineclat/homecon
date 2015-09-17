# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('log_at', models.DateTimeField(auto_now=True)),
                ('log_value', models.TextField()),
                ('siliconid', models.CharField(max_length=20)),
                ('action_taken', models.BooleanField()),
                ('action_at', models.DateTimeField()),
            ],
        ),
    ]
