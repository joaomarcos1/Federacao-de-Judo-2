from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
