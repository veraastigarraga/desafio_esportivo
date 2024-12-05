from rest_framework import serializers
from .models import Funcionarios

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Funcionarios

        filds=[
            'nome',
            'endereco',
            'telefone',
            'email',
            'idadde',
        ]