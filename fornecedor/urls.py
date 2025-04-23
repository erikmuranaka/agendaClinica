from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_fornecedor'),
    path('pesquisar/', views.pesquisar, name='pesquisar_fornecedor'),
    path('cadastrar/', views.cadastrar, name='cadastrar_fornecedor'),
    path('alterar/<int:id>/', views.alterar, name='alterar_fornecedor'),
    path('excluir/<int:id>/', views.excluir, name='excluir_fornecedor'),
]