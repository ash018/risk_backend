from rest_framework import routers
from risk.viewsets import RiskViewSet,FieldTypeViewSet



router = routers.DefaultRouter()

router.register(r'risk',RiskViewSet)
router.register(r'fieldtype',FieldTypeViewSet)
