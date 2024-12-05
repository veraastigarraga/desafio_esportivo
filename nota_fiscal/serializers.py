from rest_framework import serializers
from .models import Nota_Fiscal

class Nota_FiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nota_Fiscal

        filds=[
            'nome',
            'endereco',
            'telefone',
            'email',
            'idadde',
        ]