from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileInfo, ProfileUserInfo
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission, User
# cambiar contraseña
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from rest_framework import viewsets
from .serializers import CategoriaSerializer
from .models import Categoria, Juego, Usuario
# consumir api externa
import requests
from datetime import datetime, timedelta

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    # En la siguiente linea se especifica que metodos se podran ocupar en esta
    # view
    http_method_names = ['get']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


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


def perfil(request):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    if not is_supervisor and not is_superuser:
        usuario = Usuario.objects.get(user_ptr_id=request.user.id)
        data = {
            'form': ProfileInfo(instance=usuario)
        }
        if request.method == 'POST':
            insert_form = ProfileInfo(data=request.POST, instance=usuario)
            if insert_form.is_valid():
                insert_form.save()
                return redirect(to="perfil")
            else:
                data['insert_form'] = insert_form
    else:
        usuario = User.objects.get(id=request.user.id)
        data = {
            'form': ProfileUserInfo(instance=usuario)
        }
        if request.method == 'POST':
            insert_form = ProfileUserInfo(data=request.POST, instance=usuario)
            if insert_form.is_valid():
                insert_form.save()
                return redirect(to="perfil")
            else:
                data['insert_form'] = insert_form
    return render(request, 'app/perfil/perfil.html', data)

# Creacion de Token


@api_view(['POST'])
def logCheck(request):
    # nombre de usuario y contraseña de superusuario
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        # Busca en la base de datos al usuario
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario invalido')
    # valida la contraseña del usuario
    pdw_valid = check_password(password, user.password)
    if not pdw_valid:
        return Response('Contraseña invalido')
    # Crea el token que se asocia al usuario
    token, created = Token.objects.get_or_create(user=user)
    # Devuelve el Token
    return Response(token.key)


def show_token(request):
    Token.objects.get_or_create(user=request.user)
    token = Token.objects.filter(user_id=request.user.id)
    data = {
        'token': token
    }
    return render(request, 'app/perfil/show_token.html', data)
