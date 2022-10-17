# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTable',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('release', models.DateField()),
                ('duration', models.IntegerField()),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
    ]
