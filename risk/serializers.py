from rest_framework import serializers
from .models import Risk,Fieldtype


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = '__all__'

class FieldTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fieldtype
        fields = '__all__'