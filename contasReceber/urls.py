from django.urls import path
from . import views_template

urlpatterns = [
    path('', views_template.listar_contas_receber, name='listar_contas_receber'),
    path('cadastrar/', views_template.cadastrar_contas_receber, name='cadastrar_contas_receber'),
]