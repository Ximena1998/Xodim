import ast
import json
import time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, View, DeleteView

from .forms import EmpleadoForm, SintomatologiaForm, horarioForm, ReporteSalarioForm
from .models import Empleado, horario, Sintomatologia
from time import *
from datetime import *


@login_required(login_url='login_url')
def inicio(request):  # La que me pide peticion del navegador
    empleados = Empleado.objects.all()  # select * from Empleado

    return render(request, 'index.html', {'empleados': empleados})


@login_required(login_url='login_url')
def registroEmpleado(request):
    if request.method == 'GET':  # si la peticion viene por un metodo get lo mande en la varible form
        form = EmpleadoForm()
        contexto = {
            'form': form
        }
    else:
        form = EmpleadoForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'registroEmp.html', contexto)


def editarEmpleado(request, Cedula):
    empleado = Empleado.objects.get(cedula=Cedula)
    if request.method == 'GET':
        form = EmpleadoForm(instance=empleado)
        contexto = {
            'form': form
        }
    else:
        form = EmpleadoForm(request.POST, instance=empleado)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'index.html', contexto)


def eliminarEmpleado(request, Cedula):
    empleado = Empleado.objects.get(cedula=Cedula)
    empleado.delete()
    return redirect('index')


def fecha(request):  # primera vista
    print(time.strftime("%H:%M:%S"))  # Formato de 24 horas
    print(time.strftime("%d/%m/%y"))
    return


@login_required(login_url='login_url')
def registerAdmin(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'admin.html', {'form': form})


def registroSintomatologia(request):
    if request.method == 'GET':  # si la peticion viene por un metodo get lo mande en la varible form
        form = SintomatologiaForm()
        contexto = {
            'form': form
        }
    else:
        form = SintomatologiaForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('iniciarSesion')
    return render(request, 'registroSintomatologia.html', contexto)


def iniciarSesion(request):
    return render(request, 'inicioSesion.html')


def registroHorario(request):
    if request.method == 'GET':  # si la peticion viene por un metodo get lo mande en la varible form
        form = horarioForm()
        contexto = {
            'form': form
        }
    else:
        form = horarioForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('registrosSintomatologia')
    return render(request, 'registroHorario.html', contexto)


def estadisticas(request):
    # form = presentacionForm()
    return render(request, 'estadisticas.html')


class BiometricoCreate(TemplateView):
    template_name = 'biometrico.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'create_horary':
                horary = request.POST['horary']
                dni = request.POST['dni']
                emp = Empleado.objects.filter(cedula=dni)
                if emp.exists():
                    emp = emp[0]
                    # validar sintomas
                    fechaRegistro = datetime.now()
                    fechaRegistro_3dias = fechaRegistro - timedelta(days=3)
                    sintomas = Sintomatologia.objects.filter(sintCedula=emp,
                                                             fechaRegistro__range=[fechaRegistro_3dias, fechaRegistro])
                    validate = 0
                    if sintomas.exists():
                        data = ast.literal_eval(serializers.serialize('json', [sintomas[0], ]))[0].get('fields')
                        for k, v in data.items():
                            if type(v) == int:
                                validate += v

                    if validate > 2:
                        data = {
                            'error': 'El empleado tiene sintomas de covid 19 desde hace 3 días, no pudede registrarse su asistencia porque debe ser atendido'}
                    else:
                        h = horario.objects.filter(sintCedula=emp.cedula, fechaRegistro=datetime.now())
                        if h.exists():
                            h = h[0]
                        else:
                            h = horario()
                        h.sintCedula_id = emp.cedula
                        hour = datetime.now().strftime('%H:%M')

                        if horary == 'horaEntradaM':
                            h.horaEntradaM = hour
                        elif horary == 'horaSalidaM':
                            h.horaSalidaM = hour
                        elif horary == 'horaEntradaV':
                            h.horaEntradaV = hour
                        elif horary == 'horaSalidaV':
                            h.horaSalidaV = hour
                        h.save()
                else:
                    data = {'error': 'El empleado no se encuentra registrado'}
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de una marcación'
        return context


class BiometricoListado(ListView):
    template_name = 'biometrico_listar.html'
    model = horario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de marcaciones'
        return context


class BiometricoDelete(DeleteView):
    model = horario

    def get(self, request, *args, **kwargs):
        try:
            horario.objects.get(pk=self.kwargs['pk']).delete()
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('biometrico_listado'))


class ReporteSalarios(TemplateView):
    template_name = 'reporte_sueldos.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action', None)
        try:
            if action == 'search_report':
                data = []
                emp = request.POST['emp']
                start_date = request.POST['start_date']
                end_date = request.POST['end_date']
                h = horario.objects.filter(fechaRegistro__range=[start_date, end_date])
                if len(emp):
                    emp = Empleado.objects.get(cedula=emp)
                    h = h.filter(sintCedula_id=emp.cedula).order_by('fechaRegistro')
                    total = 0
                    for i in h:
                        horas = i.get_hours()
                        data.append({
                            'fechaRegistro': i.fechaRegistro.strftime('%d-%m-%Y'),
                            'horaEntrada': i.get_format_hour(i.horaEntradaM),
                            'horaSalidaM': i.get_format_hour(i.horaSalidaM),
                            'horaEntradaV': i.get_format_hour(i.horaEntradaV),
                            'horaSalidaV': i.get_format_hour(i.horaSalidaV),
                            'horas': horas
                        })
                        total += horas

                    data.append({
                        'fechaRegistro': '---',
                        'horaEntrada': '---',
                        'horaSalidaM': '---',
                        'horaEntradaV': '---',
                        'horaSalidaV': 'Cantidad de horas',
                        'sintCedula': '---',
                        'horas': total
                    })

                    salario = total * float(emp.valor)

                    data.append({
                        'fechaRegistro': '---',
                        'horaEntrada': '---',
                        'horaSalidaM': '---',
                        'horaEntradaV': '---',
                        'horaSalidaV': 'Salario total',
                        'sintCedula': '---',
                        'horas': format(salario, '.2f')
                    })
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Sueldos'
        context['form'] = ReporteSalarioForm()
        return context
