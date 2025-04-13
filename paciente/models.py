from django.db import models

class paciente(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    dataNascimento = models.DateField()
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome