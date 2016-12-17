# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Criteria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fname', models.CharField(max_length=25)),
                ('Lname', models.CharField(max_length=25)),
                ('Nickname', models.CharField(max_length=25)),
                ('Techlevel', models.DecimalField(default=1, max_digits=1, decimal_places=0)),
                ('Year', models.DecimalField(max_digits=2, decimal_places=0)),
                ('Rating', models.DecimalField(max_digits=1, decimal_places=0)),
                ('Bio', models.TextField(max_length=300, blank=True)),
                ('Genre', models.TextField(max_length=300, blank=True)),
                ('Address', models.TextField(max_length=300)),
                ('Instruments', models.TextField(max_length=300, blank=True)),
                ('Username', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
