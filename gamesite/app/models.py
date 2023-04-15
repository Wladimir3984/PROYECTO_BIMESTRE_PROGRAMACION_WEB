from django.db import models
from django.utils import timezone
# Create your models here.


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre


class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_venta = models.IntegerField()
    id_juego = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.id_detalle_venta


class Juego(models.Model):
    id_juego = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    precio_venta = models.IntegerField()
    stock = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    ap_paterno = models.CharField(max_length=25)
    ap_materno = models.CharField(max_length=25)
    f_nacimiento = models.DateField()
    correo = models.EmailField(max_length=254)
    direccion = models.TextField()
    usuario = models.CharField(max_length=25)
    contrasenia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaHora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_venta
