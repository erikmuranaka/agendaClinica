from django import forms
from .models import fichaMedica

class fichaMedicaForm(forms.ModelForm):
    class Meta:
        model = fichaMedica
        fields = '__all__'