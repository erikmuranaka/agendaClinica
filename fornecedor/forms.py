from django import forms
from .models import fornecedor

class fornecedorForm(forms.ModelForm):
    class Meta:
        model = fornecedor
        fields = '__all__'