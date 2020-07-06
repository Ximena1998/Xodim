from django.shortcuts import render,redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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
     template_name = 'tables.html'

class empleadoCreate(CreateView):
     model = Empleado
     form_class = EmpleadoForm
     template_name = 'index.html'
     success_url = reverse_lazy('tables')

     


class empleadoUpdate (UpdateView):
     model = Empleado
     form_class = EmpleadoForm
     template_name = 'index.html'
     success_url = reverse_lazy('index')


class empleadoDelete (DeleteView):
     model = Empleado
     template_name = 'verificacion.html'
     success_url = reverse_lazy('index')
