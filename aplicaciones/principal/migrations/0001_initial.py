# Generated by Django 3.0.8 on 2020-07-12 23:53

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('telefono', models.CharField(max_length=10)),
                ('fechaNacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=300)),
                ('cargo', models.CharField(max_length=60)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Sintomatología',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mucosidad', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(1)])),
                ('dolorMuscular', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(1)])),
                ('sintGastrointestinal', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(1)])),
                ('fechaRegistro', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('faltaAire', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(1)])),
                ('temperatura', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(1)])),
                ('tos', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(1)])),
                ('contacto', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(1), django.core.validators.MinLengthValidator(1)])),
                ('sintCedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='horario',
            fields=[
                ('idHorario', models.AutoField(primary_key=True, serialize=False)),
                ('fechaRegistro', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('horaEntradaM', models.TimeField()),
                ('horaSalidaM', models.TimeField()),
                ('horaEntradaV', models.TimeField()),
                ('horaSalidaV', models.TimeField()),
                ('horasExtra', models.IntegerField()),
                ('sintCedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Empleado')),
            ],
        ),
    ]
