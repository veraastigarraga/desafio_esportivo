from rest_framework import serializers
from .models import Produtos

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produtos

        filds=[
            'nome',
            'endereco',
            'telefone',
            'email',
            'idadde',
        ]