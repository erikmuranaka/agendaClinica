from django import forms
from .models import paciente

class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ['nome', 'cpf', 'dataNascimento', 'cep', 'endereco', 'numero', 'telefone', 'email', 'cidade', 'estado', 'ativo']
