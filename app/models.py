from django.db import models

# Create your models here.

class Cadatro_Lojas (models.Model):

    RAZAO_SOCIAL = models.CharField(max_length=100)
    CNPJ = models.IntegerField()
    NOME_FANTASIA= models.CharField(max_length=100)
    RESPONSAVEL = models.CharField(max_length=100)
    VENDEDOR = models.CharField(max_length=100)
    AUTOMACAO = models.CharField(max_length=50)
    ANALISTA = models.CharField(max_length=50)
    DATA_ATIVACAO = models.DateField()
    STATUS = models.CharField(max_length=50)