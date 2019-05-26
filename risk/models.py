from django.db import models


class Risk(models.Model):
    risk_id = models.AutoField(primary_key=True)
    risk_name = models.CharField(max_length=255)
