from django import forms
from app.models import Juego, Usuario

class InsertGameForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre', 'precio_venta', 'stock', 'id_categoria', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 2})
        }


class InsertUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
