from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm,PostForm2
from .models import *
from django.contrib.auth import *
from django.http import HttpResponseRedirect


# Create your views here.
def posts_index(request):
    p = Pay.objects.all()
    queryset_list=Pay.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list=Pay.objects.all()

    query=request.GET.get("Search")
    if query:
        queryset_list=queryset_list.all()
    return render(request,"index.html",{"p":p,"queryset_list":queryset_list})
def posts_search(request):

    return render(request,"Search.html",{})

def posts_iletisim(request):
    return render(request,"iletisim.html",{})
def posts_paylas(request):
    form=PostForm(request.POST or None,request.FILES )
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
    "form": form,
    }
    return render(request,"Paylas.html",context)

def posts_bolumler(request):
    form2=PostForm2(request.POST or None,request.FILES )
    if form2.is_valid():
        instance=form2.save(commit=False)
        instance.save()
    context={
    "form2": form2,
    }
    return render(request,"bolumler.html",context)
def bolum(request,id):
    b = Bolum.objects.filter(bolum_ID=id)
    pa = Pay.objects.filter(bolum=b)

    return render(request,"bolum.html",{"b":b,"pa":pa})

def detail(request,id):
    p = Pay.objects.filter(pk=id)
    return render(request,"detail.html",{"p":p})

def posts_bilgisayar(request):
    bol = Bolum.objects.filter(bolum_ID=2)
    pa = Pay.objects.filter(bolum=bol)

    return render(request,"bolumler/muhendislik_f/bilgisayar_m.html",{"pa":pa,"bol":bol})
def posts_insaat(request):
    bol = Bolum.objects.filter(bolum_ID=3)
    pa = Pay.objects.filter(bolum=bol)

    return render(request,"bolumler/muhendislik_f/insaat_m.html",{"pa":pa,"bol":bol})
def posts_makina(request):
    bol = Bolum.objects.filter(bolum_ID=4)
    pa = Pay.objects.filter(bolum=bol)

    return render(request,"bolumler/muhendislik_f/makina_m.html",{"pa":pa,"bol":bol})
def posts_gida(request):
    bol =Bolum.objects.filter(bolum_ID=5)
    pa = Pay.objects.filter(bolum=bol)

    return render(request,"bolumler/muhendislik_f/gida_m.html",{"pa":pa,"bol":bol})
