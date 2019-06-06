from django.test import TestCase
from ..models import Risk,Fieldtype,Field,Post

class RiskTest(TestCase):
    """Test Module For Risk"""
    def setUp(self):
        Risk.objects.create(risk_name="Test Risk")


class FieldtypeTest(TestCase):
    """Test Module For Fieldtype"""
    def setUp(self):
        Fieldtype.objects.create(fieldtype_name="Test Fieldtype")


class FieldTest(TestCase):
    """Test Module For Field"""
    def setUp(self):
        Field.objects.create(field_risk_id=1,field_fieldtype_id=1,field_label="Test Label")


class PostTest(TestCase):
    """Test Module For Post"""
    def setUp(self):
        Post.objects.create(post_id=1,post_form_id=1,post_val="Test Label")