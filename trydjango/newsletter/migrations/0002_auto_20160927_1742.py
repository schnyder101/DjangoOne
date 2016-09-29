# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 12:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='updates',
        ),
        migrations.AddField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 27, 12, 11, 28, 563000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]