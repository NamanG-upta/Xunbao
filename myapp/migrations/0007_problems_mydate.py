# Generated by Django 2.0 on 2018-01-12 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 12, 18, 34, 31, 382246)),
        ),
    ]
