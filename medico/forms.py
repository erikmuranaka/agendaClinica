from django import forms
from .models import medico

class medicoForm(forms.ModelForm):
    class Meta:
        model = medico
        fields = '__all__'