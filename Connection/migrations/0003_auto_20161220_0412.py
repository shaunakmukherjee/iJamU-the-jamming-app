# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Connection', '0002_endorsedetails_endorsement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Endorsement',
        ),
        migrations.AlterField(
            model_name='endorsedetails',
            name='Username',
            field=models.CharField(max_length=25),
        ),
    ]
