from operator import truediv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppProyectoFinalTolisanoPascaretta.models import Propietario, Inquilino, Propiedad
from AppProyectoFinalTolisanoPascaretta.forms import form_Propietarios, UserRegisterForm, UserEditForm, ChangePasswordForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render (request, "home.html")

@login_required
def Inmobiliaria (request):
    return render (request, "Inmobiliaria.html")
    
@login_required
def Propietarios (request):
    if request.method == "POST":
        propietario = Propietario(nombrecompleto = request.POST['nombrecompleto'], dni = request.POST['dni'], telefono = request.POST['telefono'], email = request.POST['email'])
        propietario.save()
        return render(request, "Inmobiliaria.html")
    return render (request, "Propietarios.html")


@login_required
def buscar_Propietarios (request):
   if request.GET['dni']:
      dni = request.GET['dni']
      Propietarios = Propietario.objects.filter(dni__icontains = dni)
      return render(request, "Propietarios.html", {"Propietarios": Propietarios})
   else:
     respuesta = "No se registró ingreso de datos"
     return HttpResponse(respuesta)

@login_required
def Inquilinos (request):
    if request.method == "POST":
        inquilino = Inquilino (nombrecompleto = request.POST["nombrecompleto"], dni = request.POST["dni"], telefono = request.POST["telefono"], email = request.POST["email"])
        inquilino.save()
        return render(request, "Inmobiliaria.html")
    return render (request, "Inquilinos.html")


@login_required
def buscar_Inquilinos (request):
   if request.GET['dni']:
      dni = request.GET['dni']
      Inquilinos = Inquilino.objects.filter(dni__icontains = dni)
      return render(request, "Inquilinos.html", {"Inquilinos": Inquilinos})
   else:
     respuesta = "No se registró ingreso de datos"
     return HttpResponse(respuesta)

@login_required
def Propiedades(request):
    if request.method == "POST":
        propiedad = Propiedad (domicilio = request.POST["domicilio"])
        propiedad.save()
        return render(request, "Inmobiliaria.html")
    return render (request, "Propiedades.html")


@login_required
def buscar_Propiedades (request):
   if request.GET['domicilio']:
      domicilio = request.GET['domicilio']
      Propiedades = Propiedad.objects.filter(domicilio__icontains = domicilio)
      return render(request, "Propiedades.html", {"Propiedades": Propiedades})
   else:
     respuesta = "No se registró ingreso de datos"
     return HttpResponse(respuesta)


@login_required
def create_propietarios (request):
    if request.method == 'POST':
        propietario = Propietario(nombrecompleto = request.POST['nombrecompleto'], dni = request.POST['dni'], telefono = request.POST['telefono'], email = request.POST['email'])
        propietario.save()
        propietarios = Propietario.objects.all()
        return render(request, "PropietariosCRUD/read_propietarios.html", {'propietarios': propietarios})
    return render(request, "PropietariosCRUD/create_propietarios.html")


@login_required    
def read_propietarios (request=None):
    propietarios = Propietario.objects.all()
    return render(request, "PropietariosCRUD/read_propietarios.html", {'propietarios': propietarios})

@login_required
def delete_propietarios (request, propietario_id):
    propietario = Propietario.objects.get(id = propietario_id)
    propietario.delete()
    propietarios = Propietario.objects.all()
    return render(request, "PropietariosCRUD/read_propietarios.html", {'propietarios': propietarios})


@login_required
def update_propietarios (request, propietario_id):
    propietario = Propietario.objects.get(id = propietario_id)

    if request.method == 'POST':
        formulario = form_Propietarios(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            propietario.nombrecompleto = informacion['nombrecompleto']
            propietario.dni = informacion['dni']
            propietario.telefono = informacion['telefono']
            propietario.email = informacion['email']
            propietario.save()
            propietarios = Propietario.objects.all() #Trae todo
            return render(request, "PropietariosCRUD/read_propietarios.html", {"propietarios": propietarios})
    else:
        formulario = form_Propietarios(initial={'nombrecompleto': propietario.nombrecompleto, 'dni': propietario.dni,'telefono': propietario.telefono, 'email': propietario.email})
    return render(request,"PropietariosCRUD/update_propietarios.html", {"formulario": formulario})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)
            
            if user is not None:
                login(request, user)
                return render(request, "Inmobiliaria.html")
            else:
                return render(request, "login.html", {'form':form})
        else:
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def registro(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save() 
            return redirect("/AppProyectoFinalTolisanoPascaretta/login")
    
        else:
            return render(request, "registro.html", {'form': form})
    
    form = UserRegisterForm()
    return render(request, 'registro.html', {'form':form})


@login_required
def editarperfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method =='POST':
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.password = form.cleaned_data.get('password')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'Inmobiliaria.html')
        else:
            return render(request, 'Inmobiliaria.html', {'form':form})
    else:
        form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email, 'password': usuario.password, 'first_name': usuario.first_name, 'last_name': usuario.last_name})         
    return render(request, 'editarperfil.html', {'form': form, 'usuario': usuario})   


@login_required
def cambiopass(request):
    usuario = request.user
    if request.method =='POST':
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'Inmobiliaria.html')
    else:
        form = ChangePasswordForm(user = request.user)
    return render(request, 'cambiopass.html' , {'form': form, 'usuario': usuario})

@login_required
def perfilView(request):
    return render(request, 'perfil.html')


            
        



