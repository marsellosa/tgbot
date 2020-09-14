from django.contrib import admin
from .models import User
from .forms import UserForm

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'first_name', 'last_name', 'username', 'language_code', 'inserted_on']
    form = UserForm


admin.site.register(User, UserAdmin)

# Register your models here.
