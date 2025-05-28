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

from groups.models import Grupo
from groups.api.serializers import GrupoSerializer

# Vista para GET, POST, PUT, DELETE en /administrador/<usuarioEscuela>/informacion/
class EscuelaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EscuelaSerializer
    lookup_field = 'nombre'

    def get_queryset(self):
        return Escuela.objects.filter(usuarioescuela__rol='administrador')

    def get_object(self):
        nombre = self.kwargs['usuarioEscuela']
        return get_object_or_404(Escuela, nombre=nombre)

# Vista de estudiantes de una escuela
class AdminEstudiantesView(generics.ListCreateAPIView):
    serializer_class = UsuarioEscuelaSerializer

    def get_queryset(self):
        return UsuarioEscuela.objects.filter(
            escuela__nombre=self.kwargs['usuarioEscuela'],
            rol='estudiante'
        )

# Vista para detalle de estudiante en una escuela
class AdminEstudianteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioEscuelaSerializer
    lookup_field = 'usuario__username'

    def get_queryset(self):
        return UsuarioEscuela.objects.filter(
            escuela__nombre=self.kwargs['usuarioEscuela'],
            rol='estudiante'
        )

# Vista para listar profesores de una escuela
class AdminProfesoresView(generics.ListCreateAPIView):
    serializer_class = UsuarioEscuelaSerializer

    def get_queryset(self):
        return UsuarioEscuela.objects.filter(
            escuela__nombre=self.kwargs['usuarioEscuela'],
            rol='profesor'
        )

# Vista para detalle de profesor en una escuela
class AdminProfesorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioEscuelaSerializer
    lookup_field = 'usuario__username'

    def get_queryset(self):
        return UsuarioEscuela.objects.filter(
            escuela__nombre=self.kwargs['usuarioEscuela'],
            rol='profesor'
        )

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



class AdminGrupoListCreateView(generics.ListCreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class AdminGrupoUsuariosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer