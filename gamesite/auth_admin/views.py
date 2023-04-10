from django.shortcuts import render
from .forms import InsertGameForm
from app.models import Juego
# Create your views here.

def agregar_juego(request):
    data = {
        'insert_form': InsertGameForm()
    }
    if request.method == 'POST':
        insert_form = InsertGameForm(data=request.POST)
        if insert_form.is_valid():
            insert_form.save()
            data['mensaje'] = "Juego agregado correctamente"
        else:
            data['mensaje'] = "Error al agregar el juego"
            data['insert_form'] = insert_form

    return render(request, 'auth_admin/juegos_crud/agregar.html', data)

def listar_juegos(request):
    juegos = Juego.objects.all()
    data = {
        'juegos':juegos
    }
    return render(request, 'auth_admin/juegos_crud/listar.html',data)
