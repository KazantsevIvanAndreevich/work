from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Role
from .models import UserProfile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class RoleForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['roles']
        widgets = {
            'roles': forms.CheckboxSelectMultiple()
        }