from rest_framework import viewsets
from .models import Risk,Fieldtype,Field,Post
from .serializers import RiskSerializer,FieldTypeSerializer,FieldSerializer,CustomFieldSerializer,PostSerializer,CustomPostSerializer,AllPostSerializer

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

    def get_queryset(self):
        req = self.request
        risk_id = req.query_params.get('risk_id')

        if risk_id:
            field = Field.objects.filter(field_risk_id__risk_id = risk_id)
            self.queryset = field
            return self.queryset
        else:
            return self.request

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CustomPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CustomPostSerializer

class AllPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = AllPostSerializer

    def get_queryset(self):
        req = self.request
        risk_id = req.query_params.get('risk_id')

        if risk_id:
            risk = Post.objects.filter(post_field_id__field_risk_id__risk_id=risk_id)
            self.queryset = risk
            return self.queryset
        else:
            return self.queryset

class MaxIdPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-post_uid')[:1]
    serializer_class = CustomPostSerializer

    def get_queryset(self):
        req = self.request
        risk_id = req.query_params.get('risk_id')

        if risk_id:
            risk = Post.objects.filter(post_field_id__field_risk_id__risk_id=risk_id).order_by('-post_uid')[:1]
            risk = risk.values('post_id')
            self.queryset = risk
            return self.queryset
        else:
            return self.queryset



