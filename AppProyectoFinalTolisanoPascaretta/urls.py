from re import template
from django.urls import path
from AppProyectoFinalTolisanoPascaretta.views import *
#from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', Inmobiliaria),
    #path('Inmobiliaria/', Inmobiliaria),
    path('Inquilinos/', Inquilinos),
    path('Propiedades/', Propiedades),
    path('Propietarios/', Propietarios),
    #path('api_Propietarios/', api_Propietarios),
    path('buscar_Propietarios/', buscar_Propietarios),
]