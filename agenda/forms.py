from django import forms
from .models import agenda

class agenda_form(forms.ModelForm):
    class Meta:
        model = agenda
        fields = '__all__'