# Archivo: groups/api/serializers.py

from rest_framework import serializers
from groups.models import Grupo, GrupoUsuario

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class GrupoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoUsuario
        fields = '__all__'
