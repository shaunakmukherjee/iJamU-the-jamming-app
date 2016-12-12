# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_auto_20161209_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User1', models.CharField(max_length=50)),
                ('Endorsed', models.BooleanField(default=b'False')),
                ('User2', models.ForeignKey(to='Login.Userdetail', to_field=b'Username')),
            ],
        ),
        migrations.RemoveField(
            model_name='request',
            name='User2',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
