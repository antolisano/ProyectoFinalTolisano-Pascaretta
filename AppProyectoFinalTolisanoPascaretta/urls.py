from re import template
from django.urls import path
from AppProyectoFinalTolisanoPascaretta.views import *



urlpatterns = [
    path('',Inmobiliaria),
    path('Inmobiliaria/',Inmobiliaria),
    path('Inquilinos/',Inquilinos),
    path('Propiedades/',Propiedades),
    path('Propietarios/',Propietarios),
    path('buscar_Propietarios/',buscar_Propietarios),
    path('buscar_Inquilinos/',buscar_Inquilinos),
    path('buscar_Propiedades/',buscar_Propiedades)
]