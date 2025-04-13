from django.db import models
from paciente.models import paciente
from medico.models import medico

class agenda(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    data = models.DateField()
    hora = models.TimeField()
    idPaciente = models.ForeignKey(paciente, on_delete=models.CASCADE, to_field='id', null=True, blank=True)
    idMedico = models.ForeignKey(medico, on_delete=models.CASCADE, to_field='id', null=True, blank=True)

    def __str__(self):
        return f"{self.data} - {self.hora}"