from rest_framework import viewsets
from .models import planoSaude
from .serializers import PlanoSaudeSerializer

class PlanoSaudeViewSet(viewsets.ModelViewSet):
    queryset = planoSaude.objects.all()
    serializer_class = PlanoSaudeSerializer
