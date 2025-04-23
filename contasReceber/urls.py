from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_cr'),
    path('pesquisar/', views.pesquisar, name='pesquisar_cr'),
    path('cadastrar/', views.cadastrar, name='cadastrar_cr'),
    path('alterar/<int:id>/', views.alterar, name='alterar_cr'),
    path('excluir/<int:id>/', views.excluir, name='excluir_cr'),
]