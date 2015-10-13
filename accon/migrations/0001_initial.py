# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ACAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('log_id', models.IntegerField(null=True)),
                ('siliconid', models.CharField(default='', max_length=20)),
                ('action_at', models.DateTimeField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='ACErrorlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('error_name', models.CharField(default='', max_length=1000)),
                ('error_at', models.DateTimeField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='ACFail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('log_id', models.IntegerField(null=True)),
                ('siliconid', models.CharField(default='', max_length=20)),
                ('fail_at', models.DateTimeField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='ACLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('log_at', models.DateTimeField(blank=True, default=None)),
                ('log_value', models.TextField(default='')),
                ('log_cmd', models.CharField(default='0', max_length=20)),
                ('log_function', models.CharField(default='0', max_length=20)),
                ('log_appid', models.CharField(default='0', max_length=20)),
                ('log_info', models.CharField(default='', max_length=256)),
                ('log_info_id', models.IntegerField(default=0, null=True)),
                ('siliconid', models.CharField(default='', max_length=20)),
                ('action_taken', models.BooleanField(default=0)),
                ('packet_str', models.CharField(default='', max_length=256)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ACSucess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('log_id', models.IntegerField(null=True)),
                ('siliconid', models.CharField(default='', max_length=20)),
                ('sucess_status', models.BooleanField(default=0)),
                ('sucess_at', models.DateTimeField(blank=True, default=None)),
                ('response_str', models.CharField(default='', max_length=256)),
            ],
        ),
    ]
