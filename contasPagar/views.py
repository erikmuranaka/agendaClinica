from rest_framework import viewsets
from .models import contasPagar
from .serializers import ContasPagarSerializer

class ContasPagarViewSet(viewsets.ModelViewSet):
    queryset = contasPagar.objects.all()
    serializer_class = ContasPagarSerializer