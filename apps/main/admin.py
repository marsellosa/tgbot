from django.contrib import admin
from .models import Settings


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'valor')


admin.site.register(Settings, SettingsAdmin)

# Register your models here.
