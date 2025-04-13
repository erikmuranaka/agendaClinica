from rest_framework import serializers
from .models import medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = medico
        fields = '__all__'