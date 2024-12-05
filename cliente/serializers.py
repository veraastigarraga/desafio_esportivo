from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente

        filds=[
            'nome',
            'endereco'
            'telefone',
            'email',
            'cpf',
        ]