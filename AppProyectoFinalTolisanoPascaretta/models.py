from django.db import models

# Create your models here.
#class Inmobiliaria(models.Model):

    

class Propietarios(models.Model):
    nombrecompleto = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

class Inquilinos(models.Model):
    nombrecompleto = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

class Propiedades():
    domicilio = models.CharField(max_length=60)


class Contratos():
    fechainicio = models.DateField()
    fechafin = models.DateField()
 

