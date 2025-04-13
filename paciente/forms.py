from django import forms
from .models import paciente

class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ['nome', 'cpf', 'dataNascimento', 'cep', 'endereco', 'numero', 'telefone', 'email']

    def clean(self):
        print(self.cleaned_data)
        
        dataNascimento = self.cleaned_data.get('dataNascimento')
        Doccpf = self.cleaned_data.get('cpf')
        Doccep = self.cleaned_data.get('cep')
        nome = self.cleaned_data.get('nome')

        print(f"Nome: {nome}")       

        print(f"Data de Nascimento: {dataNascimento}")
        print(f"CPF: {Doccpf}")
        print(f"CEP: {Doccep}")
