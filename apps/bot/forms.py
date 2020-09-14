from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'username', 'language_code', 'is_bot']
