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

# INICIO ESTUDIANTES

class EstudianteEscuelasView(generics.ListAPIView):
    serializer_class = EscuelaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs['usuarioEscuela'].lower()
        return Escuela.objects.filter(
            usuarioescuela__usuario__username=username,
            usuarioescuela__rol='estudiante'
        ).distinct()

# fin estudiantes
# INICIO PROFESOR/

# fin profesor
class EscuelasDelProfesorView(generics.ListAPIView):
    serializer_class = EscuelaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        return Escuela.objects.filter(
            usuarioescuela__usuario=usuario,
            usuarioescuela__rol='profesor'
        ).distinct()


class EscuelasDelEstudianteView(generics.ListAPIView):
    serializer_class = EscuelaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        return Escuela.objects.filter(
            usuarioescuela__usuario=usuario,
            usuarioescuela__rol='estudiante'
        ).distinct()

class ProfesorEscuelasListView(generics.ListAPIView):
    serializer_class = EscuelaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obtener las escuelas donde el usuario autenticado es profesor
        return Escuela.objects.filter(usuarioescuela__usuario=self.request.user, usuarioescuela__rol='profesor')

# Vista para GET, POST, PUT, DELETE en /administrador/<usuarioEscuela>/informacion/
class EscuelaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EscuelaSerializer
    lookup_field = 'nombre'

    def get_queryset(self):
        return Escuela.objects.filter(usuarioescuela__rol='administrador')

    def get_object(self):
        nombre = self.kwargs['usuarioEscuela']
        return get_object_or_404(Escuela, nombre=nombre)

# Crear escuelas directamente
class EscuelaCreateView(generics.CreateAPIView):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer


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