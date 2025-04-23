from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_medico'),
    path('pesquisar/', views.pesquisar, name='pesquisar_medico'),
    path('cadastrar/', views.cadastrar, name='cadastrar_medico'),
    path('alterar/<int:id>/', views.alterar, name='alterar_medico'),
    path('excluir/<int:id>/', views.excluir, name='excluir_medico'),
]