from django import forms
from .models import agenda

class agendaForm(forms.ModelForm):
    class Meta:
        model = agenda
        fields = ['data', 'hora', 'descricao', 'idMedico', 'idPaciente']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }