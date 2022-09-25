from django.db import models

# Create your models here.
#class Inmobiliaria(models.Model):

    

class Propietario(models.Model):
    nombrecompleto = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

class Inquilino(models.Model):
    nombrecompleto = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

class Propiedad(models.Model):
    domicilio = models.CharField(max_length=60)



 

