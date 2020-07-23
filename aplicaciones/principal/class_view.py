from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import EmpleadoForm, SintomatologiaForm, horarioForm
from .models import Empleado, Sintomatologia, horario
from django.db.models import Sum
import datetime
from django.http import HttpResponse


# class view():
#     dispatch: verifica el metodo de la solicitud http y ya no se necesita los iff ni get ni post
#     django los reconoce automaticamnete
#     http_not_allowed
#     para create tengo una funcion post () -- def post (self, request, arg, keyarg)


class empleadoList(ListView):
    model = Empleado, Sintomatologia
    template_name = 'index.html'


class empleadoCreate(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'registroEmp.html'
    success_url = reverse_lazy('index')


class empleadoUpdate(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'editar.html'
    success_url = reverse_lazy('index')


class empleadoDelete(DeleteView):
    model = Empleado
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')


class sintomatologiaCreate(CreateView):
    model = Sintomatologia
    form_class = SintomatologiaForm
    template_name = 'registroSintomatologia.html'
    success_url = reverse_lazy('biometrico')


class horarioCreate(CreateView):
    model = horario
    form_class = horarioForm
    template_name = 'registroHorario.html'


class estadisticas(TemplateView):
    template_name = 'estadisticas.html'

    def get_grafico(self):
        data = []
        try:
            bd = Sintomatologia.objects.all()
            numberMuco = bd.aggregate(numberMuco=Sum('mucosidad')).get('numberMuco')
            data.append(int(numberMuco))

            numberDolorM = bd.aggregate(numberDolorM=Sum('dolorMuscular')).get('numberDolorM')
            data.append(int(numberDolorM))

            numberSintG = bd.aggregate(numberSintG=Sum('sintGastrointestinal')).get('numberSintG')
            data.append(int(numberSintG))

            numberFaltaAire = bd.aggregate(numberFaltaAire=Sum('faltaAire')).get('numberFaltaAire')
            data.append(int(numberFaltaAire))

            numberTemp = bd.aggregate(numberTemp=Sum('temperatura')).get('numberTemp')
            data.append(int(numberTemp))

            numberTos = bd.aggregate(numberTos=Sum('tos')).get('numberTos')
            data.append(int(numberTos))

            numberContacto = bd.aggregate(numberContacto=Sum('contacto')).get('numberContacto')
            data.append(int(numberContacto))
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grafico'] = self.get_grafico()
        return context



class iniciarSesion(CreateView):
    model = horario
    form_class = horarioForm
    template_name = 'inicioSesion.html'
    success_url = reverse_lazy('iniciarSesion')
    


def momentoActual(request):
    respuesta = format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return render(request, 'inicioSesion.html', {"dameFecha": respuesta})
