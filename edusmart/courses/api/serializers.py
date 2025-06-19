# Archivo: courses/api/serializers.py

from rest_framework import serializers
from courses.models import Curso
from lessons.models import Leccion

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class LeccionSerializer(serializers.ModelSerializer):
    grupo = serializers.StringRelatedField(source='grupo_leccion', read_only=True)
    curso = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Leccion
        fields = [
            'id',
            'titulo',
            'contenido',
            'orden',
            'recurso_url',
            'fecha_disponible',
            'grupo',
            'curso',
        ]