from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import ContentType
from django.db import models

class PostManager(models.Manager):
    def all(self,*args,**kwargs):
        return super(PostManager,self)

def generate_file_path(instance,filename):
    return "user_{0}/%Y/%m/%d{1}".format(instance.user.id,filename)

class Bolum(models.Model):
    bolum_ID = models.IntegerField(unique=True,null=True,default=None)
    bolum=models.CharField(max_length=120)
    #updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    #timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.bolum

class Icerik(models.Model):
    icerik=models.CharField(max_length=120)
    #updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    #timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.icerik

class Pay(models.Model):
    ad_soyad=models.CharField(max_length=120)
    baslik=models.CharField(max_length=120)
    aciklama=models.TextField()
    icerik=models.ForeignKey(Icerik,null=True,default=None,on_delete=models.CASCADE)
    bolum=models.ForeignKey(Bolum,null=False,default=None,on_delete=models.CASCADE)
    #dosya=models.FileField()
    def __str__(self):
        return self.baslik


# Create your models here.
class Kayit(models.Model):
    kullanici_adi=models.CharField(max_length=15)
    parola=models.CharField(max_length=15)
    e_mail=models.EmailField(max_length=100)

    def __str__(self):
        return self.kullanici_adi




