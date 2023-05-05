from django.shortcuts import render, redirect, get_object_or_404
from .forms import InsertGameForm, InsertUserForm
from app.models import Juego, Usuario, Categoria
# Create your views here.


def agregar_juego(request):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    categorias = Categoria.objects.all()
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        data = {
            'insert_form': InsertGameForm(),
            'categorias': categorias
        }
        if request.method == 'POST':
            insert_form = InsertGameForm(
                data=request.POST, files=request.FILES)
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
    categorias = Categoria.objects.all()
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        juegos = Juego.objects.all()
        data = {
            'juegos': juegos,
            'categorias': categorias
        }
        return render(request, 'auth_admin/juegos_crud/listar.html', data)


def modificarJuego(request, id):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        juego = get_object_or_404(Juego, id_juego=id)
        data = {
            'form': InsertGameForm(instance=juego)
        }
        if request.method == 'POST':
            insert_form = InsertGameForm(
                data=request.POST, instance=juego, files=request.FILES)
            if insert_form.is_valid():
                insert_form.save()
                data['mensaje'] = "Modificado correctamente"
                return redirect(to='listar_juegos')
            else:
                data['mensaje'] = "Error al agregar el juego"
                data['insert_form'] = insert_form
        return render(request, 'auth_admin/juegos_crud/modificar.html', data)


def eliminarJuego(request):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        try:
            juego = Juego.objects.get(id_juego=request.POST.get('id_juego',''))
            juego.delete()
        except Exception as e:
            print(e)
        return render(request, 'auth_admin/juegos_crud/listar.html')


def modificar_usuario(request, id):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        usuario = get_object_or_404(Usuario, user_ptr_id=id)
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
                data['mensaje'] = "Error al agregar el usuario"
                data['insert_form'] = insert_form
        return render(request, 'auth_admin/usuario_crud/modificar.html', data)


def listar_usuarios(request):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    categorias = Categoria.objects.all()
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        usuarios = Usuario.objects.all()
        data = {
            'juegos': usuarios,
            'categorias': categorias
        }
        return render(request, 'auth_admin/usuario_crud/listar.html', data)


def eliminarUsuario(request, id):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        try:
            usuario = Usuario.objects.get(user_ptr_id=id)
            usuario.delete()
        except Exception as e:
            print(e)
        return render(request, 'auth_admin/usuario_crud/listar.html')


def agregar_usuario(request):
    is_supervisor = request.user.has_perm('auth.rol_supervisor')
    is_superuser = request.user.is_superuser
    if not is_supervisor and not is_superuser:
        return render(request, 'app/index.html')
    else:
        data = {
            'insert_form': InsertUserForm()
        }
        if request.method == 'POST':
            insert_form = InsertUserForm(data=request.POST)
            if insert_form.is_valid():
                insert_form.save()
                data['mensaje'] = "Usuario agregado correctamente"
            else:
                data['mensaje'] = "Error al agregar el usuario"
                data['insert_form'] = insert_form
        return render(request, 'auth_admin/usuario_crud/agregar.html', data)