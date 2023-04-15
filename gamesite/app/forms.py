from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class CustomUserCreationForm(UserCreationForm):
    f_nacimiento = forms.DateField(input_formats=['%d/%m/%Y'])
    direccion = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "f_nacimiento", "direccion")
