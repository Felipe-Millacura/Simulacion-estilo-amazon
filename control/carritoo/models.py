from django.db import models

# Create your models here.

class Producto(models.Model):
    Foto = models.ImageField(upload_to='Media',blank=True,null=True)
    NombreProducto = models.CharField(max_length=100)
    Descripcion = models.TextField(max_length=1000)
    Stock = models.CharField(max_length=100)
    PrecioEntrada = models.IntegerField()
    PrecioFinal = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.NombreProducto