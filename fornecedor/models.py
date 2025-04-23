from django.db import models

class fornecedor(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=100)
    razaoSocial = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    ativo = models.BooleanField(default=True)
    dataCadastro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    cidade  = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome
