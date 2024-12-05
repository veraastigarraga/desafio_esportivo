from rest_framework import serializers
from .models import Fornecedores

class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fornecedores

        filds=[
            'nome',
            'endereco'
            'telefone',
            'email',
            'produto',
        ]
