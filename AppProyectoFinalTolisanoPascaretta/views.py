from django.shortcuts import render
from django.http import HttpResponse
from AppProyectoFinalTolisanoPascaretta.models import Propietario, Inquilino, Propiedad, Contrato

# Create your views here.

def Inmobiliaria (request):
    return render (request, "Inmobiliaria.html")

def Propietarios (request):
    return render (request, "Propietarios.html")

def Inquilinos (request):
    return render (request, "Inquilinos.html")

def Propiedades(request):
    return render (request, "Propiedades.html")

def Contratos(request):
    return render (request, "Contratos.html")