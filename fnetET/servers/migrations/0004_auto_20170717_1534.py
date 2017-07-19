# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_auto_20170717_1531'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CmisServer2',
            new_name='CmisServer',
        ),
        migrations.AlterModelOptions(
            name='cmisserver',
            options={'verbose_name_plural': 'CmisServers'},
        ),
        migrations.AlterModelTable(
            name='cmisserver',
            table='CmisServer',
        ),
    ]
