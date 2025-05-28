from django.urls import path
from schools.api.views import AdminCursoDetailView, ProfesorCursoListView

urlpatterns = [
    path('<str:usuarioEscuela>/cursos/<str:nombreCurso>/', AdminCursoDetailView.as_view()),
    path('<str:usuarioEscuela>/cursos/', ProfesorCursoListView.as_view()),
]
