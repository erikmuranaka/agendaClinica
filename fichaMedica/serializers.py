from rest_framework import serializers
from .models import fichaMedica

class FichaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = fichaMedica
        fields = '__all__'