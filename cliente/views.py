from rest_framework import viewsets
from .models import Cliente

from .serializers import ClienteSerializer

class FornecedoresView(viewsets.ModelViewSet):
    queryset=Cliente.objects.all()
    serializer_class = ClienteSerializer





