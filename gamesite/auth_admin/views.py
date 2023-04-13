from django.shortcuts import render
from .forms import InsertGameForm
from app.models import Juego
# Create your views here.

def agregar_juego(request):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
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
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        juegos = Juego.objects.all()
        data = {
            'juegos':juegos
        }
        return render(request, 'auth_admin/juegos_crud/listar.html',data)
