from django.urls import path
from lessons.api.views import AdminLeccionListCreateView, AdminLeccionDetailView

urlpatterns = [
    path('<str:usuarioEscuela>/cursos/<str:nombreCurso>/lecciones/', AdminLeccionListCreateView.as_view()),
    path('<str:usuarioEscuela>/cursos/<str:nombreCurso>/lecciones/<int:pk>/', AdminLeccionDetailView.as_view()),
]
