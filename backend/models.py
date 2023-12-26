from django.db import models

# Create your models here.
class Item:
    name = models.CharField(max_legnth=100)
    description = models.CharField(max_legnth=100)
    price = models.IntegerField(max_legnth=100)