from django.shortcuts import render, redirect, get_object_or_404
from .forms import InsertGameForm, InsertUserForm
from app.models import Juego, Usuario
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
          'juegos': juegos
      }
      return render(request, 'auth_admin/juegos_crud/listar.html', data)

def modificar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)

    data = {
        'form': InsertUserForm(instance=usuario)
    }
    if request.method == 'POST':
        insert_form = InsertUserForm(
            data=request.POST, instance=usuario, files=request.FILES)
        if insert_form.is_valid():
            insert_form.save()
            data["mensaje"] = "modificado correctamente"
            return redirect(to="listar_usuarios")
        else:
            data['mensaje'] = "Error al agregar el juego"
            data['insert_form'] = insert_form
    return render(request, 'auth_admin/usuario_crud/modificar.html', data)

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    data = {
        'juegos': usuarios
    }
    return render(request, 'auth_admin/usuario_crud/listar.html', data)

