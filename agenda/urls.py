from django.urls import path
from . import views

urlpatterns = [
    path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
    path('', views.visualizar_calendario, name='visualizar_calendario'),
    path('listar_consulta/', views.listar_consulta, name='listar_consulta'),
    path('cadastrar_paciente/', views.cadastrar_paciente, name='cadastrar_paciente'),
]