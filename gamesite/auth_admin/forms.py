from django import forms
from app.models import Juego

# id_juego = m
# nombre = mod
# precio_venta
# stock = mode
# id_categoria
# descripcion
# disponible =

class InsertGameForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre', 'precio_venta', 'stock', 'id_categoria', 'descripcion', 'disponible']
