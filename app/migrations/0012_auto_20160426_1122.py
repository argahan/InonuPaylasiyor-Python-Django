# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_pay_dosya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bolum',
            name='bolum_ID',
        ),
        migrations.RemoveField(
            model_name='pay',
            name='dosya',
        ),
    ]
