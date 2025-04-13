from rest_framework import serializers
from .models import contasReceber

class ContasReceberSerializer(serializers.ModelSerializer):
    class Meta:
        model = contasReceber
        fields = '__all__'