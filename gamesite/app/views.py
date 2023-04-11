from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.


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
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        else:
            data["form"] = formulario
    return render(request, 'registration/register.html', data)
