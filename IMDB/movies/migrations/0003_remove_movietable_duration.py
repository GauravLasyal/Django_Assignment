# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20221015_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movietable',
            name='duration',
        ),
    ]
