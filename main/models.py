from django.db import models

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    stock_min = models.IntegerField()
    stock_max = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre