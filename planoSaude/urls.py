from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_plano'),
    path('pesquisar/', views.pesquisar, name='pesquisar_plano'),
    path('cadastrar/', views.cadastrar, name='cadastrar_plano'),
    path('alterar/<int:id>/', views.alterar, name='alterar_plano'),
    path('excluir/<int:id>/', views.excluir, name='excluir_plano'),
]