# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User1', models.CharField(max_length=50)),
                ('User2', models.CharField(max_length=50)),
                ('Endorsed', models.BooleanField(default=b'False')),
            ],
        ),
        migrations.CreateModel(
            name='Crequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User1', models.CharField(max_length=50)),
                ('User2', models.CharField(max_length=50)),
                ('Endorsed', models.BooleanField(default=b'False')),
            ],
        ),
    ]
