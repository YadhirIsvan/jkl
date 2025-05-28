# Archivo: lessons/api/serializers.py

from rest_framework import serializers
from lessons.models import Leccion, GrupoLeccion

class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = '__all__'

class GrupoLeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoLeccion
        fields = '__all__'
