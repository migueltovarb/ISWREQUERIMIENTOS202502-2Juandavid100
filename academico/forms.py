from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class RegistroForm(forms.ModelForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    rol = forms.ChoiceField(choices=Perfil.ROLES, label="Rol")

    class Meta:
        model = User
        fields = ['username', 'password']
