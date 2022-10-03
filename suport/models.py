from django.db import models

# Create your models here.

class suporte(models.Model):
    razao_social = models.CharField(max_length=100)   
    nome_fantasia= models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    automacao = models.CharField(max_length=50)
    cod_id = models.CharField(max_length=100)
    nome_contato = models.CharField(max_length=100)
    tel_contato = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100)
    analista = models.CharField(max_length=100)
    data_instal = models.DateTimeField()
    install = models.BooleanField()
    status = models.CharField(max_length=100)
    obs = models.TextField()
    slug = models.SlugField()