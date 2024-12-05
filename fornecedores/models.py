from django.db import models

# Create your models here.
class Fornecedores(models.Model):
    nome=models.CharField(max_length=100)
    endereço=models.IntegerField()
    telefone=models.IntegerField()
    email=models.IntegerField()
    produtos=models.IntegerField()

