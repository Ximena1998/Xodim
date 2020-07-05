from django.db import models

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

def __str__(self): #self recibe todo metodo de una clase
    return self.nombres
    