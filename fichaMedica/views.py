from rest_framework import viewsets
from .models import fichaMedica
from .serializers import FichaMedicaSerializer

class FichaMedicaViewSet(viewsets.ModelViewSet):
    queryset = fichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer
