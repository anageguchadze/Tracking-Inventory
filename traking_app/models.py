from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.name