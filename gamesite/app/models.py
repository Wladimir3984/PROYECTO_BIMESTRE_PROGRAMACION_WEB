from django.db import models
# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

class DetalleVenta(models.Model):
    id_detalle_venta = models.IntegerField(primary_key=True)
    id_venta = models.IntegerField()
    id_juego = models.IntegerField()
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    descuento = models.IntegerField()

class Juego(models.Model):
    id_juego = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    precio_venta = models.IntegerField()
    stock = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=225)
    disponible = models.CharField(max_length=1)

class MetodoPago(models.Model):
    id_metodo_pago = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    ap_paterno = models.CharField(max_length=25)
    ap_materno = models.CharField(max_length=25)
    f_nacimiento = models.DateField()
    correo = models.CharField(max_length=25)
    direccion = models.CharField(max_length=225)
    usuario = models.CharField(max_length=25)
    contrasenia = models.CharField(max_length=100)
    is_admin = models.CharField(max_length=1)

class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    impuesto = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateField()
