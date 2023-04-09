from django.shortcuts import render
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