# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160419_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bolum',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='cevaplar',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='cevaplar',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='ders_notlari',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='ders_notlari',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='ders_videolari',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='ders_videolari',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='duyuru',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='duyuru',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='fakulte',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='gorusler',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='gorusler',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='sikayet',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='sikayet',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='sorular',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='sorular',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='vize_final',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='vize_final',
            name='updated',
        ),
        migrations.AddField(
            model_name='pay',
            name='aciklama',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pay',
            name='baslik',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ders_notlari',
            name='dosya',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='ders_videolari',
            name='dosya',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vize_final',
            name='dosya',
            field=models.FileField(upload_to=''),
        ),
    ]
