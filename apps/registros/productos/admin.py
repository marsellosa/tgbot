from django.contrib import admin
from .models import Categoria, Sabor, Pais
from admin_auto_filters.filters import AutocompleteFilter


class CategoriaFilter(AutocompleteFilter):
    title = 'Categoria'  # display title
    field_name = 'categoria'  # name of the foreign key field


class CategoriaAdmin(admin.ModelAdmin):
    # this is required for django's autocomplete functionality
    search_fields = ['nombre']


class SaborAdmin(admin.ModelAdmin):
    list_filter = [CategoriaFilter]


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Sabor, SaborAdmin)
admin.site.register(Pais)
