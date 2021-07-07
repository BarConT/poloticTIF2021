from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['titulo', 'imagen', 'categoria', 'descripcion', 'precio'] 
