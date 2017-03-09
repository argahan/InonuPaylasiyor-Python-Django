from django.contrib import admin
from django.core import urlresolvers

# Register your models here.
from .models import Bolum
from .models import Pay
from .models import Icerik
class ModelAdmin(admin.ModelAdmin):

    class Meta:
       model=Bolum,
       model=Pay,
       model=Icerik,

admin.site.register(Bolum,ModelAdmin),
admin.site.register(Pay,ModelAdmin),
admin.site.register(Icerik,ModelAdmin),

class AAdmin(admin.ModelAdmin):
    list_display = ["bolum","link_to_Bolum"]
    def link_to_Bolum(self, obj):
        link=urlresolvers.reverse("admin:app_Bolum_change", args=[obj.Bolum.id])
        return u'<a href="%s">%s</a>' % (link,obj.Bolum.bolum)
    link_to_Bolum.allow_tags=True
