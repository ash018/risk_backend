from rest_framework import serializers
from .models import Risk,Fieldtype,Field,Post

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = '__all__'

class FieldTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fieldtype
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields='__all__'

class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
        depth = 1

class PostSerializer(serializers.ModelSerializer):
    field = FieldSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class CustomPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id']
        depth = 2

class AllPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 2