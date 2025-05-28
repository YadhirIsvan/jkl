# Archivo: schools/api/serializers.py

from rest_framework import serializers
from schools.models import Escuela

class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = '__all__'
