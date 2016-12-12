# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_auto_20161208_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User1', models.CharField(max_length=50)),
                ('Endorsed', models.BooleanField(default=b'False')),
                ('User2', models.ForeignKey(to='Login.Userdetail', to_field=b'Username')),
            ],
        ),
        migrations.AlterField(
            model_name='connection',
            name='User2',
            field=models.ForeignKey(to='Login.Userdetail', to_field=b'Username'),
        ),
    ]
