from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_medico, name='login_medico')
]