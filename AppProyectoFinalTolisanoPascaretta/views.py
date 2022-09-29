from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppProyectoFinalTolisanoPascaretta.models import Propietario, Inquilino, Propiedad
from AppProyectoFinalTolisanoPascaretta.forms import form_Propietarios

# Create your views here.


def Inmobiliaria (request):
    return render (request, "Inmobiliaria.html")

def Propietarios (request):
    if request.method == "POST":
        propietario = Propietario(nombrecompleto = request.POST['nombrecompleto'], dni = request.POST['dni'], telefono = request.POST['telefono'], email = request.POST['email'])
        propietario.save()
        return render(request, "Inmobiliaria.html")
    return render (request, "Propietarios.html")

def buscar_Propietarios (request):
   if request.GET['dni']:
      dni = request.GET['dni']
      Propietarios = Propietario.objects.filter(dni__icontains = dni)
      return render(request, "Propietarios.html", {"Propietarios": Propietarios})
   else:
     respuesta = "No se registró ingreso de datos"
     return HttpResponse(respuesta)

def Inquilinos (request):
    if request.method == "POST":
        inquilino = Inquilino (nombrecompleto = request.POST["nombrecompleto"], dni = request.POST["dni"], telefono = request.POST["telefono"], email = request.POST["email"])
        inquilino.save()
        return render(request, "Inmobiliaria.html")
    return render (request, "Inquilinos.html")

def buscar_Inquilinos (request):
   if request.GET['dni']:
      dni = request.GET['dni']
      Inquilinos = Propietario.objects.filter(dni__icontains = dni)
      return render(request, "Inquilinos.html", {"Inquilinos": Inquilinos})
   else:
     respuesta = "No se registró ingreso de datos"
     return HttpResponse(respuesta)

def Propiedades(request):
    if request.method == "POST":
        propiedad = Propiedad (domicilio = request.POST["domicilio"])
        propiedad.save()
        return render(request, "Inmobiliaria.html")
    return render (request, "Propiedades.html")

    