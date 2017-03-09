# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160423_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='dosya',
            field=models.FileField(verbose_name='Dosya', default=None, upload_to=app.models.generate_file_path),
        ),
    ]
