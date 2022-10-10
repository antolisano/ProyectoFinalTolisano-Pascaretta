from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class form_Propietarios(forms.Form):
    nombrecompleto = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    telefono = forms.CharField()
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Usuario'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Apellido'}))

    class Meta:
        model = User
        fields = ['username','email','password', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}    
