from re import template
from django.urls import path
from AppProyectoFinalTolisanoPascaretta.views import *
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('home/' ,home),
    path('',home),
    path('about/', about),
    #path('', views.Inmobiliaria, name = 'Inmobiliaria'),
    path('Inmobiliaria/',Inmobiliaria),
    path('Inquilinos/',Inquilinos),
    path('Propiedades/',Propiedades),
    path('Propietarios/',Propietarios),
    path('buscar_Propietarios/',buscar_Propietarios),
    path('buscar_Inquilinos/',buscar_Inquilinos),
    path('buscar_Propiedades/',buscar_Propiedades),
    path('create_propietarios/',create_propietarios),
    path('read_propietarios/',read_propietarios),
    path('delete_propietarios/<propietario_id>',delete_propietarios),
    path('update_propietarios/<propietario_id>',update_propietarios),
    path('create_inquilinos/',create_inquilinos),
    path('read_inquilinos/',read_inquilinos),
    path('delete_inquilinos/<inquilino_id>',delete_inquilinos),
    path('update_inquilinos/<inquilino_id>',update_inquilinos),
    path('create_propiedades/',create_propiedades),
    path('read_propiedades/',read_propiedades),
    path('delete_propiedades/<propiedad_id>',delete_propiedades),
    path('update_propiedades/<propiedad_id>',update_propiedades),
    path('login/',login_request),
    path('registro/',registro),
    path('logout/' ,LogoutView.as_view(template_name = 'home.html'), name = 'Logout'),
    path('perfil/',perfilView),
    path('perfil/editarperfil/',editarperfil),
    path('perfil/cambiopass/',cambiopass),
    path('perfil/cambiofotoperfil/' ,AgregarFoto)
    


    
]