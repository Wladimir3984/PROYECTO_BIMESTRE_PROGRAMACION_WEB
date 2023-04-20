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
from .models import Categoria
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
    context = {'is_supervisor': is_supervisor, 'is_superuser': is_superuser}
    return render(request, 'app/index.html', context)

def aventura(request):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    is_superuser = request.user.is_superuser
    context = {'is_supervisor': is_supervisor, 'is_superuser': is_superuser}
    return render(request, 'app/aventura.html', context)

def plataforma(request):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    is_superuser = request.user.is_superuser
    context = {'is_supervisor': is_supervisor, 'is_superuser': is_superuser}
    return render(request, 'app/plataforma.html', context)

def guerra(request):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    is_superuser = request.user.is_superuser
    context = {'is_supervisor': is_supervisor, 'is_superuser': is_superuser}
    return render(request, 'app/guerra.html', context)

def terror(request):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    is_superuser = request.user.is_superuser
    context = {'is_supervisor': is_supervisor, 'is_superuser': is_superuser}
    return render(request, 'app/terror.html', context)

def rpg(request):
    is_supervisor = request.user.groups.filter(name='supervisor').exists()
    is_superuser = request.user.is_superuser
    context = {'is_supervisor': is_supervisor, 'is_superuser': is_superuser}
    return render(request, 'app/rpg.html', context)
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
