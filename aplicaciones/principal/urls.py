from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from aplicaciones.principal.class_view import empleadoList, empleadoCreate, empleadoUpdate, empleadoDelete
from aplicaciones.principal.models import Empleado

urlpatterns = [
   path('register/',views.registerAdmin, name = 'register_url'),
   path('login/',LoginView.as_view(),name = 'login_url'),
   path('logout/',LogoutView.as_view(next_page = 'login_url'),name = 'logout'),
    path('registro/',empleadoCreate.as_view(), name = 'registroEmp'),

    path('listaEmpleado/',empleadoList.as_view(model=Empleado), name='index' ),

    path('editarEmpleado/<str:pk>/', empleadoUpdate.as_view(), name = 'editarEmpleado'),

    path('eliminarEmpleado/<str:pk>/', empleadoDelete.as_view(), name = 'eliminarEmpleado'),
]