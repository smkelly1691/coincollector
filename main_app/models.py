from django.db import models
from django.urls import reverse

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coin_id': self.id})