from django.urls import path
from AppProyectoFinalTolisanoPascaretta.views import *
from ProyectoFinalTolisanoPascaretta.ProyectoFinalTolisanoPascaretta.view import home


urlpatterns = [
    path('', home),
    path('Contratos/', Contratos),
    path('Inmobiliaria/', Inmobiliaria),
    path('Inquilinos/', Inquilinos),
    path('Propiedades/', Propiedades),
    path('Propietarios/', Propietarios),
]