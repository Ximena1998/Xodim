
"""xidomin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function viewss
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
from aplicaciones.principal.views import inicio, registroEmpleado, editarEmpleado, eliminarEmpleado, fecha
from aplicaciones.principal.class_view import empleadoList, empleadoCreate, empleadoUpdate, empleadoDelete


urlpatterns = [
    path('admin/', admin.site.urls),
   
  #  path('', inicio,name ='index'), lo cambiamos paa las clases
    path('registro/',empleadoCreate.as_view(), name = 'index'),
    #path('registroEmpleado/',registroEmpleado, name='registroEmpleado' ),
    path('listaEmpleado/',empleadoList.as_view(), name='tables' ),
    #path('editarEmpleado/<str:Cedula>/', editarEmpleado, name = 'editarEmpleado'),
    path('editarEmpleado/<str:pk>/', empleadoUpdate.as_view(), name = 'editarEmpleado'),
   # path('eliminarEmpleado/<str:Cedula>/', eliminarEmpleado, name = 'eliminarEmpleado')
    path('eliminarEmpleado/<str:pk>/', empleadoDelete.as_view(), name = 'eliminarEmpleado'),
    
    #url(r'^$', LoginView.as_view(template_name='landing.html'), name='landing')
    #path('',LoginView.as_view(template_name= 'login.html'), name = 'login'),
    path('administrador/',include('aplicaciones.principal.urls')),
   
   

]
