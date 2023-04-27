from django.db import models
from django.urls import reverse
# Create your models here.

class Asset(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    description = models.TextField(max_length=250)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('investments_detail', kwargs={'asset_id': self.id})
