# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160423_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='dosya',
            field=models.FileField(upload_to=app.models.generate_file_path, default=None, verbose_name='Dosya'),
        ),
    ]
