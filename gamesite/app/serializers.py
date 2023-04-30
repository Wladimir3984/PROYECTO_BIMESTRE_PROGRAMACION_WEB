from .models import Categoria
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

class CategoriaSerializer(serializers.ModelSerializer):
    # Los siguientes campos los dejaremos como solo lectura ya que no queremos
    # que accedan a estos
    id_categoria = serializers.IntegerField()
    nombre = serializers.CharField()
    permission_classes = [IsAuthenticated]
    class Meta:
        model = Categoria
        fields = ('__all__')
