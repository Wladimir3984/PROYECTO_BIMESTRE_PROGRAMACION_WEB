# Generated by Django 4.1.7 on 2023-04-07 23:46
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalle_venta', models.AutoField(primary_key=True, serialize=False)),
                ('id_venta', models.IntegerField()),
                ('id_juego', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descuento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('ap_paterno', models.CharField(max_length=25)),
                ('ap_materno', models.CharField(max_length=25)),
                ('f_nacimiento', models.DateField()),
                ('correo', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=225)),
                ('usuario', models.CharField(max_length=25)),
                ('contrasenia', models.CharField(max_length=100)),
                ('is_admin', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('impuesto', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fecha', models.DateField()),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.metodopago')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id_juego', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('precio_venta', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('descripcion', models.CharField(max_length=225)),
                ('disponible', models.CharField(max_length=1)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
            ],
        ),
    ]
