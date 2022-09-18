from django.db import models

# Create your models here.
class Doctores(models.Model):
    nombrecompleto = models.CharField(max_length=50)
    matricula = models.IntegerField()
    especialidad = models.CharField()

class Pacientes(models.Model):
    nombrecompleto = models.CharField(max_length=50)
    dni = models.IntegerField()
    fechanacimiento = models.DateField()

class Especialidades(models.Model):
    nombre = models.CharField()

