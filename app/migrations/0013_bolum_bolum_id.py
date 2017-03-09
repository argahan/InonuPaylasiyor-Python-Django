# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160426_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolum',
            name='bolum_ID',
            field=models.IntegerField(default=None, unique=True, null=True),
        ),
    ]
