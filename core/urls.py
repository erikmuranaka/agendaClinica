from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a área de administração do Django
    path('paciente/', include('paciente.urls')),  # Rotas do aplicativo Paciente
    path('agenda/', include('agenda.urls')),  # Rotas do aplicativo Agenda
    path('fornecedor/', include('fornecedor.urls')),  # Rotas do aplicativo Fornecedor
    path('planosaude/', include('planoSaude.urls')),  # Rotas do aplicativo PlanoSaude
    path('fichamedica/', include('fichaMedica.urls')),  # Rotas do aplicativo FichaMedica
    path('contasreceber/', include('contasReceber.urls')),  # Rotas do aplicativo ContasReceber
    path('contaspagar/', include('contasPagar.urls')),  # Rotas do aplicativo ContasPagar
    path('medico/', include('medico.urls')),  # Rotas do aplicativo Medico
]