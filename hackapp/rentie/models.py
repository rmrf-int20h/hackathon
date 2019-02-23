from django.db import models

# Create your models here.
class Item(models.Model):
     name = models.CharField(max_length=50)
     description = models.TextField(max_length=500)
     price = models.FloatField(default=0.0, min_value=0.0)
     rating = models.FloatField(default=0.0, min_value=0.0, max_value=5.0)
     in_rent = models.BooleanField(default=False)
     passport_id = models.ForeignKey(ItemPassport, on_delete=models.CASCADE)


class ItemPassport(models.Model):
    description = models.TextField()
