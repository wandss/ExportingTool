# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmisServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_name', models.CharField(max_length=50)),
                ('server_address', models.CharField(max_length=100)),
                ('date_creation', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'CmisServer',
            },
        ),
    ]
