# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iter', '0006_auto_20161127_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connections',
            name='User2',
            field=models.CharField(max_length=50),
        ),
    ]
