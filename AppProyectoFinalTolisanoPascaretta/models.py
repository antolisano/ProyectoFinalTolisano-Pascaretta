from unittest.util import _MAX_LENGTH
from django.db import models

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

    def __str__(self):
       return f"Dirección: {self.domicilio}"

 

