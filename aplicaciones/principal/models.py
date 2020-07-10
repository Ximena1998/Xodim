from django.db import models
from datetime import date
# Create your models here.

class Empleado(models.Model):
    cedula = models.CharField(max_length=10, primary_key = True)
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    telefono = models.CharField(max_length = 10)
    fechaNacimiento = models.DateField ()
    direccion = models.CharField(max_length = 300)
    cargo = models.CharField(max_length = 60)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

#def __str__(self): #self recibe todo metodo de una clase
 #   return self.nombres
    
class Sintomatología(models.Model):
    id = models.AutoField(primary_key = True)
    mucosidad = models.CharField(max_length = 2)
    dolorMuscular = models.CharField(max_length = 2)
    sintGastrointestinal = models.CharField(max_length = 2)
    fechaRegistro = models.DateField(("Date"), default=date.today)
    faltaAire = models.CharField(max_length = 2)
    temperatura = models.CharField(max_length = 2)
    tos = models.CharField(max_length = 2)
    contacto = models.CharField(max_length = 2)
    sintCedula = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class horario(models.Model):
    idHorario = models.AutoField(primary_key = True)
    fechaRegistro = models.DateField(("Date"), default=date.today)
    horaEntradaM = models.TimeField (auto_now = False)
    horaSalidaM = models.TimeField (auto_now = False)
    horaEntradaV = models.TimeField (auto_now = False)
    horaSalidaV = models.TimeField (auto_now = False)
    horasExtra = models.IntegerField()
    sintCedula = models.ForeignKey(Empleado, on_delete=models.CASCADE)
"""
class presentacion(models.Model):
    fecha = models.DateField(("Date"), default=date.today)
"""