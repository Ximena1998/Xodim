# Generated by Django 3.0.7 on 2020-06-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
    ]
