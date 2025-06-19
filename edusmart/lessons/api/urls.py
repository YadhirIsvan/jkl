from django.urls import path
from lessons.api.views import AdminLeccionListCreateView, AdminLeccionDetailView, EstudianteLeccionesCursoView


urlpatterns = [
    path('<str:usuarioEscuela>/cursos/<str:nombreCurso>/lecciones/', AdminLeccionListCreateView.as_view()),
    path('<str:usuarioEscuela>/cursos/<str:nombreCurso>/lecciones/<int:pk>/', AdminLeccionDetailView.as_view()),

    # ESTUDIANTES

    path('est/<str:usuarioEscuela>/cursos/<slug:nombreCurso>/lecciones/', EstudianteLeccionesCursoView.as_view(), name='lecciones-del-curso'
    )
]
