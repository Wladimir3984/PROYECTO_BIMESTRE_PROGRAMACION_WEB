from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission
# cambiar contraseña
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from rest_framework import viewsets
from .serializers import CategoriaSerializer
from .models import Categoria, Juego
# consumir api externa
import requests
from datetime import datetime, timedelta

# Create your views here.


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    # En la siguiente linea se especifica que metodos se podran ocupar en esta
    # view
    http_method_names = ['get']


class MyPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'app/password_change_form.html'
    success_url = '/'


def index(request):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    is_superuser = request.user.is_superuser
    categorias = Categoria.objects.all()
    # consumir api externa
    # Calcular las fechas de inicio y fin
    current_year = datetime.now().year
    start_date = datetime(current_year, 1, 1)
    end_date = datetime(current_year + 1, 1, 1) - timedelta(days=1)

    end_date_str = end_date.strftime('%Y-%m-%d')
    start_date_str = start_date.strftime('%Y-%m-%d')

    # Construir la URL de la API
    url = f'https://api.rawg.io/api/games?key=562fd14dbe0a49b28a86b8078f8cc6a4&dates={start_date_str},{end_date_str}&ordering=-rating&page_size=10'

    # Hacer la solicitud a la API
    response = requests.get(url)
    games_data = response.json()
    context = {
        'is_supervisor': is_supervisor,
        'is_superuser': is_superuser,
        'categorias': categorias,
        'games': games_data['results'],
    }
    return render(request, 'app/index.html', context)


def categoria(request, nombre):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    is_superuser = request.user.is_superuser
    categorias = Categoria.objects.all()
    categoria_actual = Categoria.objects.get(nombre=nombre)
    juegos = Juego.objects.filter(id_categoria=categoria_actual)
    context = {'is_supervisor': is_supervisor, 'is_superuser': is_superuser, 'categorias': categorias,
               'juegos': juegos, 'categoria_actual': categoria_actual}
    return render(request, 'app/categoria.html', context)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            # Get the existing permission
            permission = Permission.objects.get(codename='rol_user')

            # Add the permission to the user
            user.user_permissions.add(permission)

            user = authenticate(
                username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        else:
            data["form"] = formulario
    return render(request, 'registration/register.html', data)
