# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_auto_20161209_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='User2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='crequest',
            name='User2',
            field=models.CharField(max_length=50),
        ),
    ]
