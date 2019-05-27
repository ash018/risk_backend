from rest_framework import routers
from risk.viewsets import RiskViewSet,FieldTypeViewSet,FieldViewSet,CustomFieldViewSet,PostViewSet


router = routers.DefaultRouter()

router.register(r'risk',RiskViewSet)
router.register(r'fieldtype',FieldTypeViewSet)
router.register(r'field',FieldViewSet)
router.register(r'cform',CustomFieldViewSet)
router.register(r'post',PostViewSet)