from django.db import models
from django.urls import reverse

class product(models.Model):
    name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Description = models.TextField(max_length=100)
    
    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
