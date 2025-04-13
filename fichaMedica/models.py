from django.db import models
from medico.models import medico
from paciente.models import paciente

class fichaMedica(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    idMedico = models.ForeignKey(medico, on_delete=models.CASCADE, null=True, blank=True)
    idPaciente = models.ForeignKey(paciente, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
