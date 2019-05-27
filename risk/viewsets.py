from rest_framework import viewsets
from .models import Risk,Fieldtype,Field
from .serializers import RiskSerializer,FieldTypeSerializer,FieldSerializer,CustomFieldSerializer,PostSerializer

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

class FieldTypeViewSet(viewsets.ModelViewSet):
    queryset = Fieldtype.objects.all()
    serializer_class = FieldTypeSerializer

class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

class CustomFieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = CustomFieldSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = PostSerializer

