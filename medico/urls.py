from django.urls import path
from . import views_template

urlpatterns = [
    path('', views_template.listar_medicos, name='listar_medicos'),
    path('cadastrar/', views_template.cadastrar_medico, name='cadastrar_medico'),
]