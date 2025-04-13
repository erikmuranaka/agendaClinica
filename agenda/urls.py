from django.urls import path
from . import views_template

urlpatterns = [
    path('', views_template.listar_agendas, name='listar_agendas'),
    path('cadastrar/', views_template.cadastrar_agenda, name='cadastrar_agenda'),
]