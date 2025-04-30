from rest_framework import viewsets
from .models import agenda
from .serializers import AgendaSerializer

class ContasReceberViewSet(viewsets.ModelViewSet):
    queryset = agenda.objects.all()
    serializer_class = AgendaSerializer