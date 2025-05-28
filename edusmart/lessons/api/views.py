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

# Vista para /administrador/<usuarioEscuela>/cursos/<nombreCurso>/lecciones/
class AdminLeccionListCreateView(generics.ListCreateAPIView):
    serializer_class = GrupoLeccionSerializer

    def get_queryset(self):
        return GrupoLeccion.objects.filter(
            curso__nombre=self.kwargs['nombreCurso'],
            curso__escuela__nombre=self.kwargs['usuarioEscuela']
        )

# Vista para /administrador/<usuarioEscuela>/cursos/<nombreCurso>/lecciones/<int:pk>/
class AdminLeccionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeccionSerializer

    def get_queryset(self):
        return Leccion.objects.filter(
            grupo_leccion__curso__nombre=self.kwargs['nombreCurso'],
            grupo_leccion__curso__escuela__nombre=self.kwargs['usuarioEscuela']
        )
