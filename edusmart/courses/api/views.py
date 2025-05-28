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


# Vista para /profesor/<usuarioEscuela>/cursos/
class ProfesorCursoListView(generics.ListAPIView):
    serializer_class = CursoSerializer

    def get_queryset(self):
        return Curso.objects.filter(
            escuela__nombre=self.kwargs['usuarioEscuela'],
            id_docente=self.request.user
        )

# Vista para /administrador/<usuarioEscuela>/cursos/<nombreCurso>/
class AdminCursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CursoSerializer
    lookup_field = 'nombre'

    def get_queryset(self):
        return Curso.objects.filter(
            escuela__nombre=self.kwargs['usuarioEscuela']
        )
