from operator import truediv
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
      Inquilinos = Inquilino.objects.filter(dni__icontains = dni)
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


def buscar_Propiedades (request):
   if request.GET['domicilio']:
      domicilio = request.GET['domicilio']
      Propiedades = Propiedad.objects.filter(domicilio__icontains = domicilio)
      return render(request, "Propiedades.html", {"Propiedades": Propiedades})
   else:
     respuesta = "No se registró ingreso de datos"
     return HttpResponse(respuesta)    

def create_propietarios (request):
    if request.method == 'POST':
        propietario = Propietario(nombrecompleto = request.POST['nombrecompleto'], dni = request.POST['dni'], telefono = request.POST['telefono'], email = request.POST['email'])
        propietario.save()
        propietarios = Propietario.objects.all()
        return render(request, "PropietariosCRUD/read_propietarios.html", {'propietarios': propietarios})
    return render(request, "PropietariosCRUD/create_propietarios.html")

    
def read_propietarios (request):
    propietarios = Propietario.objects.all()
    return render(request, "PropietariosCRUD/read_propietarios.html", {'propietarios': propietarios})

def delete_propietarios (request):
    return False

def update_propietarios (request):
    return False



