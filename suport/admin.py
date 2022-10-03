from django.contrib import admin
from .models import suporte

# Register your models here.
class suporteAdmin(admin.ModelAdmin):
    ...
admin.site.register(suporte, suporteAdmin)
