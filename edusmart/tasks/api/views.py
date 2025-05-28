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

# Vista para /administrador/<usuarioEscuela>/cursos/<nombreCurso>/tareas/
class AdminTareaListCreateView(generics.ListCreateAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        return Tarea.objects.filter(
            leccion__grupo_leccion__curso__nombre=self.kwargs['nombreCurso'],
            leccion__grupo_leccion__curso__escuela__nombre=self.kwargs['usuarioEscuela']
        )

# Vista para /administrador/<usuarioEscuela>/cursos/<nombreCurso>/tareas/<int:pk>/
class AdminTareaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        return Tarea.objects.filter(
            leccion__grupo_leccion__curso__nombre=self.kwargs['nombreCurso'],
            leccion__grupo_leccion__curso__escuela__nombre=self.kwargs['usuarioEscuela']
        )
