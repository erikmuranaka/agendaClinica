from django import forms
from .models import planoSaude

class planoSaudeForm(forms.ModelForm):
    class Meta:
        model = planoSaude
        fields = '__all__'