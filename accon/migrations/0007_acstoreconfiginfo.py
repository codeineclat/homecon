# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accon', '0006_acdetails_current_scale'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACStoreconfiginfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('xbee_name', models.CharField(max_length=256, default='')),
                ('xbee_number', models.CharField(max_length=256, default='')),
            ],
        ),
    ]
