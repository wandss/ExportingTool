# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20170717_1528'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CmisServer',
            new_name='CmisServer2',
        ),
    ]
