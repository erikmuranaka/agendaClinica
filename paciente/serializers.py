from rest_framework import serializers
from .models import paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        fields = ['nome', 'cpf', 'dataNascimento', 'cep', 'endereco', 'numero', 'telefone', 'email', 'cidade', 'estado', 'ativo']