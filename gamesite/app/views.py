from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, 'app/index.html')
def aventura(request):
    return render(request, 'app/aventura.html')
def plataforma(request):
    return render(request, 'app/plataforma.html')
def guerra(request):
    return render(request, 'app/guerra.html')
def terror(request):
    return render(request, 'app/terror.html')
def rpg(request):
    return render(request, 'app/rpg.html')
def loggin(request):
    return render(request, 'app/loggin.html')
def formulario(request):
    return render(request, 'app/formulario.html')
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
