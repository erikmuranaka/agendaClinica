from django.urls import path
from . import views_template

urlpatterns = [
    path('', views_template.listar_contas_pagar, name='listar_contas_pagar'),
    path('cadastrar/', views_template.cadastrar_contas_pagar, name='cadastrar_contas_pagar'),
]