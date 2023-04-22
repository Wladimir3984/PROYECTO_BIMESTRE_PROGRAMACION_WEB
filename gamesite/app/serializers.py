from .models import Categoria
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    #Los siguientes campos los dejaremos como solo lectura ya que no queremos que accedan a estos
    id_categoria = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(read_only=True)
    class Meta:
        model = Categoria
        fields = ('__all__')
