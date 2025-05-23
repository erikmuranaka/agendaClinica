from rest_framework import serializers
from .models import agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = agenda
        fields = ['data', 'hora', 'descricao', 'idMedico', 'idPaciente']