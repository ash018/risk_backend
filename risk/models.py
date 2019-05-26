from django.db import models


class Risk(models.Model):
    risk_id = models.AutoField(primary_key=True)
    risk_name = models.CharField(max_length=255)

class Fieldtype(models.Model):
    fieldtype_id = models.AutoField(primary_key=True)
    fieldtype_name = models.CharField(max_length=255)