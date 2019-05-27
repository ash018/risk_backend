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
    class Meta:
        model=Post
        fields = ['post_uid','post_val']

    #post_val = serializers.SerializerMethodField('get_post_val')
