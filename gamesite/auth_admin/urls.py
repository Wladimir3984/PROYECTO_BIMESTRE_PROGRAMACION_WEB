
from django.urls import path
from .views import agregar_juego, listar_juegos


urlpatterns = [
    path('usroetnu2342342348rnteoenturoeuo213/', agregar_juego, name='agregar_juego'),
    path('usroetnu2342342348rnteoenturoeuo214/', listar_juegos, name="listar_juegos"),
]

