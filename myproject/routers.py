from rest_framework import routers
from risk.viewsets import RiskViewSet,FieldTypeViewSet,FieldViewSet,CustomFieldViewSet,PostViewSet,CustomPostViewSet,MaxIdPostViewSet


router = routers.DefaultRouter()

router.register(r'risk',RiskViewSet)
router.register(r'fieldtype',FieldTypeViewSet)
router.register(r'field',FieldViewSet)
router.register(r'cform',CustomFieldViewSet)
router.register(r'post',PostViewSet)
router.register(r'cpost',CustomPostViewSet)
router.register(r'maxpost',MaxIdPostViewSet)