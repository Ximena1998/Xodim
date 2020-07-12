"""xodin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from aplicaciones.principal.views import inicio, registroEmpleado, editarEmpleado, eliminarEmpleado, fecha, iniciarSesion, registroSintomatologia, registroHorario, estadisticas
from aplicaciones.principal.class_view import empleadoList, empleadoCreate, empleadoUpdate, empleadoDelete,  sintomatologiaCreate, horarioCreate, estadisticas
from django.views.generic import TemplateView
from aplicaciones.principal.models import Empleado
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('registro/',empleadoCreate.as_view(), name = 'index'),
    #path('listaEmpleado/',empleadoList.as_view(model=Empleado), name='tables'),
    #path('editarEmpleado/<str:pk>/', empleadoUpdate.as_view(), name = 'editarEmpleado'),
    #path('eliminarEmpleado/<str:pk>/', empleadoDelete.as_view(), name = 'eliminarEmpleado'),
    path('', iniciarSesion ,name = 'iniciarSesion'),
    path('registroSintomatologia/', sintomatologiaCreate.as_view(), name = 'registroSintomatologia'),
    path('registroHorario/', horarioCreate.as_view(), name = 'registroHorario'),
    path('administrador/',include('aplicaciones.principal.urls')),
    path('estadisticas/', estadisticas.as_view() ,name = 'estadisticas'),
]
