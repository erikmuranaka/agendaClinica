from django import forms
from .models import contasPagar

class ContasPagarForm(forms.ModelForm):
    class Meta:
        model = contasPagar
        fields = '__all__'