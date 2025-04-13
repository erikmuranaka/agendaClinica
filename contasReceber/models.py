from django.db import models
from medico.models import medico
from paciente.models import paciente
from planoSaude.models import planoSaude

class contasReceber(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    idMedico = models.ForeignKey(medico, on_delete=models.CASCADE, null=True, blank=True)
    dataEmissao = models.DateField()
    idPaciente = models.ForeignKey(paciente, on_delete=models.CASCADE, null=True, blank=True)
    idPlanos = models.ForeignKey(planoSaude, on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.CharField(max_length=100)
    tipoConta = models.CharField(max_length=100)
    dataVencimento = models.DateField()
    dataPagamento = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    formaPagamento = models.CharField(max_length=100)
    centroReceita = models.CharField(max_length=100)
    dataRecebimento = models.DateField()
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descricao
