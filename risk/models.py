from django.db import models


class Risk(models.Model):
    risk_id = models.AutoField(primary_key=True)
    risk_name = models.CharField(max_length=255)

class Fieldtype(models.Model):
    fieldtype_id = models.AutoField(primary_key=True)
    fieldtype_name = models.CharField(max_length=255)


class Field(models.Model):
    field_id = models.AutoField(primary_key=True)
    field_risk_id = models.ForeignKey(Risk,on_delete=models.CASCADE,)
    field_fieldtype_id = models.ForeignKey(Fieldtype,on_delete=models.CASCADE,)
    field_label = models.CharField(max_length=255)


class Post(models.Model):
    post_uid = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    post_form_id = models.ForeignKey(Field,on_delete=models.CASCADE,)
    post_val = models.CharField(max_length=255)


