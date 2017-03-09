# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160422_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolum',
            name='bolum_ID',
            field=models.IntegerField(null=True, default=None, unique=True),
        ),
        migrations.AlterField(
            model_name='pay',
            name='dosya',
            field=models.FileField(verbose_name='Dosya', upload_to=app.models.generate_file_path),
        ),
    ]
