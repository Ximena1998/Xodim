from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import datetime, timedelta


# Create your models here.

class Empleado(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=10)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=300)
    cargo = models.CharField(max_length=60)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{} / {}'.format(self.nombres, format(self.valor, '.2f'))


class Sintomatologia(models.Model):
    SI = 1
    NO = 0
    Opciones = [
        (SI, 'Si'),
        (NO, 'No'),

    ]
    id = models.AutoField(primary_key=True)
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
    idHorario = models.AutoField(primary_key=True)
    fechaRegistro = models.DateField(("Date"), default=date.today)
    horaEntradaM = models.TimeField(auto_now=False, null=True, blank=True)
    horaSalidaM = models.TimeField(auto_now=False, null=True, blank=True)
    horaEntradaV = models.TimeField(auto_now=False, null=True, blank=True)
    horaSalidaV = models.TimeField(auto_now=False, null=True, blank=True)
    horasExtra = models.IntegerField(default=0)
    sintCedula = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def get_format_hour(self, hour):
        try:
            return hour.strftime('%H:%M %p')
        except:
            pass
        return '---'

    def get_hours(self):
        try:
            horas_entrada_m = timedelta(hours=self.horaEntradaM.hour, minutes=self.horaEntradaM.minute)
            horas_salida_m = timedelta(hours=self.horaSalidaM.hour, minutes=self.horaSalidaM.minute)
            horas_total_m = horas_salida_m - horas_entrada_m
            # print(horas_total_m)
            horas_entrada_s = timedelta(hours=self.horaEntradaV.hour, minutes=self.horaEntradaV.minute)
            horas_salida_s = timedelta(hours=self.horaSalidaV.hour, minutes=self.horaSalidaV.minute)
            horas_total_s = horas_salida_s - horas_entrada_s
            print(horas_total_s)
            return (horas_total_m + horas_total_s).total_seconds() / 3600
        except:
            pass
        return 0


