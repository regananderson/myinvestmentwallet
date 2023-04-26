from django.db import models

# Create your models here.

class Asset(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    description = models.TextField(max_length=250)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name

