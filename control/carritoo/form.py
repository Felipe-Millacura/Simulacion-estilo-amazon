from django import forms
from .models import Producto

class ProductForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=('Foto','NombreProducto','Descripcion','Stock','PrecioEntrada','PrecioFinal')

