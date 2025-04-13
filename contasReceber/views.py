from rest_framework import viewsets
from .models import contasReceber
from .serializers import ContasReceberSerializer

class ContasReceberViewSet(viewsets.ModelViewSet):
    queryset = contasReceber.objects.all()
    serializer_class = ContasReceberSerializer