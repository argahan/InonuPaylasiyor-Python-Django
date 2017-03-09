# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_pay_dosya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ders_notlari',
            name='bolum',
        ),
        migrations.RemoveField(
            model_name='ders_videolari',
            name='bolum',
        ),
        migrations.RemoveField(
            model_name='duyuru',
            name='bolum',
        ),
        migrations.RemoveField(
            model_name='vize_final',
            name='bolum',
        ),
        migrations.DeleteModel(
            name='Ders_Notlari',
        ),
        migrations.DeleteModel(
            name='Ders_Videolari',
        ),
        migrations.DeleteModel(
            name='Duyuru',
        ),
        migrations.DeleteModel(
            name='Vize_Final',
        ),
    ]
