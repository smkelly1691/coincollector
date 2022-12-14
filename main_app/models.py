from django.db import models
from django.urls import reverse

TYPES = (
    ('L1', 'Personal Research'),
    ('L2', 'Informal Dealer Appraisal'),
    ('L3', 'Numismatic Guaranty Corporation Appraisal')
)

# Create your models here.

class Show(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    date = models.DateField('Show Date')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shows_detail", kwargs={"pk": self.id})
    

class Coin(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    shows = models.ManyToManyField(Show)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coin_id': self.id})
    
class Appraising(models.Model):
    date = models.DateField('Appraisal Date')
    type = models.CharField(
        max_length=2,
        choices=TYPES,
        default=TYPES[0][0]
    )
    
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']