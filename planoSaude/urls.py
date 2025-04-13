from django.urls import path
from . import views_template

urlpatterns = [
    path('', views_template.listar_plano_saude, name='listar_plano_saude'),
    path('cadastrar/', views_template.cadastrar_plano_saude, name='cadastrar_plano_saude'),
    path('alterar/<int:plano_id>/', views_template.alterar_plano_saude, name='alterar_plano_saude'),
    path('excluir/<int:plano_id>/', views_template.excluir_plano_saude, name='excluir_plano_saude'),
]