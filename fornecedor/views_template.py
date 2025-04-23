from rest_framework import viewsets
from .models import fornecedor
from .serializers import FornecedorSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = fornecedor.objects.all()
    serializer_class = FornecedorSerializer