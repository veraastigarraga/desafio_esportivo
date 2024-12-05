from rest_framework import viewsets
from .models import Professor
from .serializers import Nota_FiscalSerializer

class Nota_FiscalView(viewsets.ModelViewSet):
    queryset=Nota_FiscalSerializer.objects.all()
    serializer_class = Nota_FiscalSerializer


