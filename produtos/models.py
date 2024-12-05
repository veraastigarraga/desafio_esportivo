from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome=models.CharField(max_length=100)
    cor=models.IntegerField()
    altura=models.IntegerField()
    largura=models.IntegerField()
    tamanho=models.IntegerField()

