from django.shortcuts import render,redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import EmpleadoForm
from .models import Empleado

#class view():
#     dispatch: verifica el metodo de la solicitud http y ya no se necesita los iff ni get ni post
#     django los reconoce automaticamnete
#     http_not_allowed
#     para create tengo una funcion post () -- def post (self, request, arg, keyarg)

class empleadoList (ListView):
     model = Empleado
     template_name = 'index.html'

class empleadoCreate(CreateView):
     model = Empleado
     form_class = EmpleadoForm
     template_name = 'registroEmpleado.html'
     success_url = reverse_lazy('index')

class empleadoUpdate (UpdateView):
     model = Empleado
     form_class = EmpleadoForm
     template_name = 'registroEmpleado.html'
     success_url = reverse_lazy('index')

class empleadoDelete (DeleteView):
     model = Empleado
     template_name = 'verificacion.html'
     success_url = reverse_lazy('index')
