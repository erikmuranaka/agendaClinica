from rest_framework import serializers
from .models import contasPagar

class ContasPagarSerializer(serializers.ModelSerializer):
    class Meta:
        model = contasPagar
        fields = '__all__'