from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_paciente'),
    path('pesquisar/', views.pesquisar, name='pesquisar_paciente'),
    path('cadastrar/', views.cadastrar, name='cadastrar_paciente'),
    path('alterar/<int:id>/', views.alterar, name='alterar_paciente'),
    path('excluir/<int:id>/', views.excluir, name='excluir_paciente'),
]