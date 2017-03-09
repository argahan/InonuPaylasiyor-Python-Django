from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.posts_index),
    url(r'^iletisim/$', views.posts_iletisim),
    url(r'^paylas/$', views.posts_paylas),
    url(r'^bolumler/$', views.posts_bolumler),
    url(r'^detail/(\d*)/$',views.detail),
   # url(r'^bilgisayar_muh/$',views.posts_bilgisayar),
    #url(r'^gida_muh/$',views.posts_gida),
    #url(r'^insaat_muh/$',views.posts_insaat),
    #url(r'^makina_muh/$',views.posts_makina),
    url(r'^bolum/(\d*)/$',views.bolum),
    url(r'^search/$', views.posts_search),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
