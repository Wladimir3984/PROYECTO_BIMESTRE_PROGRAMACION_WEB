from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission
#cambiar contraseña
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from rest_framework import viewsets
from .serializers import CategoriaSerializer
from .models import Categoria, Juego
# Create your views here.


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class MyPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'app/password_change_form.html'
    success_url = '/'


def index(request):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    is_superuser = request.user.is_superuser
    categorias = Categoria.objects.all()
    context = {'is_supervisor': is_supervisor, 'is_superuser': is_superuser, 'categorias': categorias}
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

            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        else:
            data["form"] = formulario
    return render(request, 'registration/register.html', data)
