from django.db import models
from fornecedor.models import fornecedor

class contasPagar(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    idFornecedor = models.ForeignKey(fornecedor, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    dataVencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    formaPagamento = models.CharField(max_length=100)
    dataPagamento = models.DateField(null=True, blank=True)
    centroCusto = models.CharField(max_length=100)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descricao