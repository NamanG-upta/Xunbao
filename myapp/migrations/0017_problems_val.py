# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-07 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='val',
            field=models.IntegerField(default=1),
        ),
    ]
