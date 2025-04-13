from django.urls import path
from . import views_template

urlpatterns = [
    path('', views_template.listar_fornecedores, name='listar_fornecedores'),
    path('cadastrar/', views_template.cadastrar_fornecedor, name='cadastrar_fornecedor'),
]