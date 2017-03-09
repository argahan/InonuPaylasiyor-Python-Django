# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160419_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='fakulte',
            field=models.ForeignKey(to='app.fakulte', null=True, default=None),
        ),
    ]
