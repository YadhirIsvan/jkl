# Archivo: schools/api/views.py (ejemplo de una app con vistas genéricas DRF adaptadas)

from rest_framework import generics, mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from schools.models import Escuela
from schools.api.serializers import EscuelaSerializer
from user_app.models import UsuarioEscuela
from user_app.api.serializers import UsuarioEscuelaSerializer
from courses.models import Curso
from courses.api.serializers import CursoSerializer
from lessons.models import Leccion, GrupoLeccion
from lessons.api.serializers import LeccionSerializer, GrupoLeccionSerializer
from tasks.models import Tarea
from tasks.api.serializers import TareaSerializer
from groups.models import Grupo, GrupoUsuario
from groups.api.serializers import GrupoSerializer, GrupoUsuarioSerializer

# Vista para /administrador/<usuarioEscuela>/grupos/
class AdminGrupoListCreateView(generics.ListCreateAPIView):
    serializer_class = GrupoSerializer

    def get_queryset(self):
        return Grupo.objects.filter(
            escuela__nombre=self.kwargs['usuarioEscuela']
        )

# Vista para /administrador/<usuarioEscuela>/grupos/<nombre>/
class AdminGrupoUsuariosDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GrupoUsuarioSerializer
    lookup_field = 'grupo__nombre'

    def get_queryset(self):
        return GrupoUsuario.objects.filter(
            grupo__escuela__nombre=self.kwargs['usuarioEscuela']
        )
