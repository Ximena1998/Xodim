from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from aplicaciones.principal.class_view import empleadoList, empleadoCreate, empleadoUpdate, empleadoDelete

urlpatterns = [
   path('register/',views.registerAdmin, name = 'register_url'),
   path('login/',LoginView.as_view(),name = 'login_url'),
   path('logout/',LogoutView.as_view(next_page = 'login_url'),name = 'logout'),
    path('registro/',empleadoCreate.as_view(), name = 'index'),
    #path('registroEmpleado/',registroEmpleado, name='registroEmpleado' ),
    path('listaEmpleado/',empleadoList.as_view(), name='tables' ),
    #path('editarEmpleado/<str:Cedula>/', editarEmpleado, name = 'editarEmpleado'),
    path('editarEmpleado/<str:pk>/', empleadoUpdate.as_view(), name = 'editarEmpleado'),
   # path('eliminarEmpleado/<str:Cedula>/', eliminarEmpleado, name = 'eliminarEmpleado')
    path('eliminarEmpleado/<str:pk>/', empleadoDelete.as_view(), name = 'eliminarEmpleado'),
]