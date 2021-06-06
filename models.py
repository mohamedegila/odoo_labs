from django.db import models


# Create your models here.

class Medicine(models.Model):
    _description = 'Medicine description'

    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    manufacturer = models.CharField(max_length=255)
