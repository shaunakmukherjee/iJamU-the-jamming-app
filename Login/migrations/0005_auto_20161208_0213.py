# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='User2',
            field=models.ForeignKey(to='Login.Userdetail', to_field=b'Username', unique=True),
        ),
    ]
