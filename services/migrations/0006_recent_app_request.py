# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20150929_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recent_App_Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('app_id', models.CharField(max_length=20, default='')),
                ('app_name', models.CharField(max_length=20, default='')),
            ],
        ),
    ]
