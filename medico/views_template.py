from rest_framework import viewsets
from .models import medico
from .serializers import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = medico.objects.all()
    serializer_class = MedicoSerializer
