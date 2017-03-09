# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_pay_fakulte'),
    ]

    operations = [
        migrations.CreateModel(
            name='icerik',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('icerik', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Kayit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('kullanici_adi', models.CharField(max_length=15)),
                ('parola', models.CharField(max_length=15)),
                ('e_mail', models.EmailField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Cevaplar',
        ),
        migrations.DeleteModel(
            name='Gorusler',
        ),
        migrations.DeleteModel(
            name='Sikayet',
        ),
        migrations.RemoveField(
            model_name='sorular',
            name='bolum',
        ),
        migrations.RemoveField(
            model_name='ders_notlari',
            name='fakulte',
        ),
        migrations.RemoveField(
            model_name='ders_videolari',
            name='fakulte',
        ),
        migrations.RemoveField(
            model_name='duyuru',
            name='fakulte',
        ),
        migrations.RemoveField(
            model_name='pay',
            name='fakulte',
        ),
        migrations.RemoveField(
            model_name='vize_final',
            name='fakulte',
        ),
        migrations.AddField(
            model_name='pay',
            name='bolum',
            field=models.ForeignKey(default=None, null=True, to='app.bolum'),
        ),
        migrations.AddField(
            model_name='pay',
            name='dosya',
            field=models.FileField(upload_to='', default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='fakulte',
        ),
        migrations.DeleteModel(
            name='Sorular',
        ),
        migrations.AddField(
            model_name='pay',
            name='icerik',
            field=models.ForeignKey(default=None, null=True, to='app.icerik'),
        ),
    ]
