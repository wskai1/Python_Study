from django.db import models

# Create your models here.
class Tab1(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    age = models.FloatField()
