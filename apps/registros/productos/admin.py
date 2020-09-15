from django.contrib import admin
from .models import Categoria, Sabor, Pais, Detalles


class CategoriaAdmin(admin.ModelAdmin):
    # this is required for django's autocomplete functionality
    list_display = ['nombre', 'pais', 'activo']
   


class SaborAdmin(admin.ModelAdmin):
    list_display = ['sabor', 'categoria', 'descripcion']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Sabor, SaborAdmin)
admin.site.register(Pais)
admin.site.register(Detalles)
