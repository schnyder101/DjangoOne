# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20160927_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
