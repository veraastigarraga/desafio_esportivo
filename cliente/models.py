from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome=models.CharField(max_length=100)
    endereço=models.IntegerField()
    telefone=models.IntegerField()
    email=models.IntegerField()
    idade=models.IntegerField()
