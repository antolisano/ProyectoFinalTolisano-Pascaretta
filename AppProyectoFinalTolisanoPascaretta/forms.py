from dataclasses import fields
import email
from django import forms



class form_Propietarios(forms.Form):
    nombreyapellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    telefono = forms.CharField()
    email = forms.EmailField()
