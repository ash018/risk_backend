from rest_framework import viewsets
from .models import Risk,Fieldtype
from .serializers import RiskSerializer,FieldTypeSerializer


class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

class FieldTypeViewSet(viewsets.ModelViewSet):
    queryset = Fieldtype.objects.all()
    serializer_class = FieldTypeSerializer
