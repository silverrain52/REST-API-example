from django.db import models

class Finance(models.Model):
    country = models.CharField(max_length=30)
    standard = models.CharField(max_length=30)
    change_dollar = models.CharField(max_length=30)
