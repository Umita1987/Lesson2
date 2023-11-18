from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)
# Create your models here.
