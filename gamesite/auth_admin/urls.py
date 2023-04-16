
from django.urls import path
from .views import agregar_juego, listar_juegos, modificar_usuario, listar_usuarios, modificarJuego, eliminarJuego, eliminarUsuario, agregar_usuario

#http://.. ..  .. /oneturoetu234tnr4234rntrt234rnt234ntroeturoetur884oetnun/

urlpatterns = [
    path('usroetnu2342342348rnteoenturoeuo213/', agregar_juego, name='agregar_juego'),
    path('usroetnu2342342348rnteoenturoeuo213/<id>/', eliminarJuego, name='eliminarJuego'),
    path('usroetnu2342342348rnteoenturoeuo214/', listar_juegos, name='listar_juegos'),
    path('usroetnu2342342348rnteoenturoeuo214/<id>/', modificarJuego, name='modificarJuego'),
    
    path('usroetnu2342342348rnteoenturoeuo215/', listar_usuarios, name='listar_usuarios'),
    path('usroetnu2342342348rnteoenturoeuo215/<id>/', modificar_usuario, name='modificar_usuario'),
    path('usroetnu2342342348rnteoenturoeuo216/', agregar_usuario, name='agregar_usuario'),
    path('usroetnu2342342348rnteoenturoeuo216/<id>/', eliminarUsuario, name='eliminarUsuario'),
]

