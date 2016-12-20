# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Connection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endorsedetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Techlevel', models.DecimalField(default=1, max_digits=1, decimal_places=0)),
                ('Rating', models.DecimalField(max_digits=1, decimal_places=0)),
                ('Comments', models.TextField(max_length=300, blank=True)),
                ('Nickname', models.CharField(max_length=25)),
                ('Username', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endorsement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User1', models.CharField(max_length=50)),
                ('User2', models.CharField(max_length=50)),
                ('Endorsed', models.BooleanField(default=b'True')),
            ],
        ),
    ]
