# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0009_auto_20161209_2329'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Connection',
        ),
        migrations.DeleteModel(
            name='Crequest',
        ),
        migrations.DeleteModel(
            name='Search',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='Username',
        ),
        migrations.DeleteModel(
            name='Userdetail',
        ),
    ]
