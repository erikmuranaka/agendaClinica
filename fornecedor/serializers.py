from rest_framework import serializers
from .models import fornecedor

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = fornecedor
        fields = '__all__'