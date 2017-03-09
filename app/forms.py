from django import forms

from .models import Pay
from .models import Bolum
from .models import Kayit
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):
    class Meta:
        model=Pay

        fields= [
        "ad_soyad",
        "baslik",
        "aciklama",
        "bolum",
        "icerik",
        #"dosya",
        ]
class PostForm2(forms.ModelForm):
    class Meta:
        model=Pay

        fields=[
            "bolum"
        ]



