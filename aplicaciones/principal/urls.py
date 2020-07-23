from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from aplicaciones.principal.class_view import empleadoUpdate, empleadoDelete, estadisticas
from aplicaciones.principal.views import inicio, registroEmpleado, BiometricoCreate, BiometricoListado, \
    BiometricoDelete, ReporteSalarios
from . import views

urlpatterns = [
    path('register/', views.registerAdmin, name='register_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout'),
    path('registro/', registroEmpleado, name='registroEmp'),
    path('listaEmpleado/', inicio, name='index'),
    path('editarEmpleado/<str:pk>/', empleadoUpdate.as_view(), name='editarEmpleado'),
    path('eliminarEmpleado/<str:pk>/', empleadoDelete.as_view(), name='eliminarEmpleado'),
    path('estadisticas/', estadisticas.as_view(), name='estadisticas'),
    path('estadisticas/', estadisticas.as_view(), name='estadisticas'),
    path('biometrico/', BiometricoCreate.as_view(), name='biometrico'),
    path('biometrico/listado/', BiometricoListado.as_view(), name='biometrico_listado'),
    path('biometrico/borrar/<int:pk>/', BiometricoDelete.as_view(), name='biometrico_delete'),
    path('reporte/salarios/', ReporteSalarios.as_view(), name='reporte_salarios'),
]
