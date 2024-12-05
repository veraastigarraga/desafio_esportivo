from rest_framework import viewsets
from .models import Fornecedores

from .serializers import FornecedoresSerializer

class FornecedoresView(viewsets.ModelViewSet):
    queryset=Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer




