from rest_framework import serializers
from .models import planoSaude

class PlanoSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = planoSaude
        fields = '__all__'