# Archivo: schools/api/views.py (ejemplo de una app con vistas genéricas DRF adaptadas)

from rest_framework import generics, mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from schools.models import Escuela
from schools.api.serializers import EscuelaSerializer
from user_app.models import UsuarioEscuela
from user_app.api.serializers import UsuarioEscuelaSerializer
from courses.models import Curso, CursoUsuario
from courses.api.serializers import CursoSerializer, LeccionSerializer
from lessons.models import Leccion

# INICIO ESTUDIANTES

class EstudianteLeccionDetailView(generics.RetrieveAPIView):
    serializer_class = LeccionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Leccion.objects.filter(
            curso__slug=self.kwargs['nombreCurso'],
            curso__escuela__username=self.kwargs['usuarioEscuela'],
            curso__cursousuario__usuario=self.request.user  # Aquí estaba el error, antes pusiste cursousuario directo en Leccion
        )
    
class EstudianteCursoDetailViewEstudiante(generics.RetrieveAPIView):
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'
    lookup_url_kwarg = 'slugCurso'  # <--- este valor viene de la URL

    def get_queryset(self):
        return Curso.objects.filter(
            escuela__username=self.kwargs['usuarioEscuela'],
            cursousuario__usuario=self.request.user  # accediendo al modelo intermedio CursoUsuario
        )



# NOS MUESTRA LOS CURSOS A LOS QUE ESTA INCRITO CADA ESTUDIANTE
# /estudiante/<str:usuarioEscuela>/
class EstudianteCursosView(generics.ListAPIView):
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username_escuela = self.kwargs['usuarioEscuela'].lower()
        usuario = self.request.user

        # Buscar escuela por su username único
        try:
            escuela = Escuela.objects.get(username=username_escuela)
        except Escuela.DoesNotExist:
            return Curso.objects.none()

        # Obtener cursos relacionados a ese usuario y esa escuela
        cursos_ids = CursoUsuario.objects.filter(
            usuario=usuario,
            curso__escuela=escuela
        ).values_list('curso_id', flat=True)

        return Curso.objects.filter(id__in=cursos_ids)

# INICIO PROFESORES
class EstudianteCursoDetailView(generics.RetrieveAPIView):
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        usuario = self.request.user

        usuario_escuela = get_object_or_404(
            UsuarioEscuela,
            usuario=usuario,
            escuela__slug=self.kwargs['usuarioEscuela'],
            rol='estudiante'
        )

        curso = get_object_or_404(
            Curso,
            escuela=usuario_escuela.escuela,
            slug=self.kwargs['nombreCurso']
        )

        return curso

# fin profesores


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
