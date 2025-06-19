# Archivo: schools/api/serializers.py

from rest_framework import serializers
from schools.models import Escuela
from user_app.models import UsuarioEscuela



class UsuarioEscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEscuela
        fields = '__all__'



class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = '__all__'
