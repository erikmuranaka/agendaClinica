from django.db import models
from medico.models import medico
from paciente.models import paciente

class agenda(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.CharField(max_length=255, null=True, blank=True)
    idMedico = models.ForeignKey(medico, on_delete=models.CASCADE, to_field='id', null=True, blank=True)
    idPaciente = models.ForeignKey(paciente, on_delete=models.CASCADE, to_field='id', null=True, blank=True)

    def __str__(self):
        return f"{self.data} - {self.hora}"
    
    