# Archivo: courses/api/serializers.py

from rest_framework import serializers
from courses.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
