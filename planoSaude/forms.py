from django import forms
from .models import planoSaude

class planoSaudeForm(forms.ModelForm):
    class Meta:
        model = planoSaude
        fields = ['id', 'nome', 'cnpj', 'telefone', 'email', 'endereco', 'cidade', 'estado', 'cep', 'numero', 'ativo']