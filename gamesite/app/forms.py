from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomUserCreationForm(UserCreationForm):
    f_nacimiento = forms.DateField(widget=DateInput)
    direccion = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

    class Meta:
        model = Usuario
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "f_nacimiento",
            "direccion")

class ProfileInfo(forms.ModelForm):
    f_nacimiento = forms.DateField(widget=DateInput)
    direccion = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

    class Meta:
        model = Usuario
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "f_nacimiento",
            "direccion")