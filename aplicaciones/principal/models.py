from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator, MaxLengthValidator
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
    SI = 1
    NO = 0
    Opciones = [
        (SI, 'Si'),
        (NO, 'No'),
       
    ]
    id = models.AutoField(primary_key = True)
    mucosidad = models.IntegerField(choices=Opciones)
    dolorMuscular = models.IntegerField(choices=Opciones)
    sintGastrointestinal = models.IntegerField(choices=Opciones)
    fechaRegistro = models.DateField(("Date"), default=date.today)
    faltaAire = models.IntegerField(choices=Opciones)
    temperatura = models.IntegerField(choices=Opciones)
    tos = models.IntegerField(choices=Opciones)
    contacto = models.IntegerField(choices=Opciones)
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