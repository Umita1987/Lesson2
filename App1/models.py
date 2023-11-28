from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Photo")

    def __str__(self):
        return self.title
