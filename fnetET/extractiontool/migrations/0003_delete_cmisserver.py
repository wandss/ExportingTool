# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extractiontool', '0002_cmisserver_date_creation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CmisServer',
        ),
    ]
