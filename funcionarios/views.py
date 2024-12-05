from rest_framework import viewsets
from .models import Funcionarios
from .serializers import FuncionariosSerializer

class FuncionariosView(viewsets.ModelViewSet):
    queryset=Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer



