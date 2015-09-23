# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playpause', '0009_fail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('upload_at', models.DateTimeField(default=None, blank=True)),
                ('songfile', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
        ),
    ]
