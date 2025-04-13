from rest_framework import viewsets
from .models import paciente
from .serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = paciente.objects.all()
    serializer_class = PacienteSerializer