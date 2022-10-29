from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class Inmobiliaria(models.Model):

    

class Propietario(models.Model):
    nombrecompleto = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
       return f"Nombre Completo: {self.nombrecompleto} - Dni: {self.dni} - Telefono: {self.telefono} - Email: {self.email}"

class Inquilino(models.Model):
    nombrecompleto = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
       return f"Nombre Completo: {self.nombrecompleto} - Dni: {self.dni} - Telefono: {self.telefono} - Email: {self.email}"

class Propiedad(models.Model):
    domicilio = models.CharField(max_length=60)
    propietario = models.ForeignKey(Propietario, null = True, blank = True, on_delete = models.CASCADE)
    inquilino = models.ForeignKey(Inquilino, null = True, blank = True, on_delete = models.RESTRICT)
    def __str__(self):
        return f"Dirección: {self.domicilio} - Propietario: {self.propietario} - Inquilino: {self.inquilino}"
       

class FotoPerfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null = True, blank = True)
 

