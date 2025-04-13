from django import forms
from .models import contasReceber

class contasReceberForm(forms.ModelForm):
    class Meta:
        model = contasReceber
        fields = '__all__'