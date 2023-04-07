from django.db import models
# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre
