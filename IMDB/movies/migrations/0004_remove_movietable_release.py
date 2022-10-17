# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movietable_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movietable',
            name='release',
        ),
    ]
