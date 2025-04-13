from django.urls import path
from . import views_template

urlpatterns = [
    path('', views_template.listar_fichas_medica, name='listar_fichas_medica'),
    path('cadastrar/', views_template.cadastrar_ficha_medica, name='cadastrar_ficha_medica'),
]