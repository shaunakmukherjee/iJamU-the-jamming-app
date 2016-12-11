# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0008_auto_20161209_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='Bio',
            field=models.TextField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='Genre',
            field=models.TextField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='Instruments',
            field=models.TextField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='Techlevel',
            field=models.DecimalField(default=1, max_digits=1, decimal_places=0),
        ),
    ]
