from django.shortcuts import render,redirect
from .models import Empleado, Sintomatología # presentacion
from .forms import EmpleadoForm, SintomatologiaForm, horarioForm # presentacionForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import time


def inicio(request): #La que me pide peticion del navegador
     empleados = Empleado.objects.all() #select * from Empleado
     print (empleados)
     contexto = {
           'empleados':empleados
     }
     return render (request, 'index.html', contexto)

def registroEmpleado(request):
    if request.method == 'GET': #si la peticion viene por un metodo get lo mande en la varible form
        form = EmpleadoForm()
        contexto = {
             'form':form
        }
    else:
        form = EmpleadoForm(request.POST)
        contexto = {
             'form':form
        }
        if form.is_valid():
             form.save()
             return redirect('index')
    return render (request, 'registroEmp.html', contexto)
    

def editarEmpleado(request, Cedula):
     empleado = Empleado.objects.get(cedula = Cedula)
     if request.method == 'GET':
         form = EmpleadoForm (instance = empleado)
         contexto = {
             'form':form
         }
     else: 
         form = EmpleadoForm (request.POST, instance = empleado)
         contexto = {
             'form':form
         }
         if form.is_valid():
             form.save()
             return redirect('index')
     return render (request, 'index.html', contexto)


def eliminarEmpleado (request, Cedula):
     empleado = Empleado.objects.get(cedula = Cedula)
     empleado.delete()
     return redirect ('index') 

def fecha(request): # primera vista
    print(time.strftime("%H:%M:%S")) #Formato de 24 horas
    print (time.strftime("%d/%m/%y"))
    return 


def registerAdmin(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'admin.html',{'form':form})



def registroSintomatologia(request):
    if request.method == 'GET': #si la peticion viene por un metodo get lo mande en la varible form
        form = SintomatologiaForm()
        contexto = {
             'form':form
        }
    else:
        form = SintomatologiaForm(request.POST)
        contexto = {
             'form':form
        }
        if form.is_valid():
             form.save()
             return redirect('iniciarSesion')
    return render (request, 'registroSintomatologia.html', contexto)

def iniciarSesion (request):
    #form = presentacionForm()
    return render (request, 'inicioSesion.html')



def registroHorario(request):
    if request.method == 'GET': #si la peticion viene por un metodo get lo mande en la varible form
        form = horarioForm()
        contexto = {
             'form':form
        }
    else:
        form = horarioForm(request.POST)
        contexto = {
             'form':form
        }
        if form.is_valid():
             form.save()
             return redirect('registrosSintomatologia')
    return render (request, 'registroHorario.html', contexto)