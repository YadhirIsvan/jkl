from django.urls import path
from schools.api.views import AdminCursoDetailView, ProfesorCursoListView
from courses.api.views import EstudianteCursoDetailView, EstudianteCursosView, EstudianteCursoDetailViewEstudiante, EstudianteLeccionDetailView

urlpatterns = [
    path('adm/<str:usuarioEscuela>/cursos/<str:nombreCurso>/', AdminCursoDetailView.as_view()),
    
    # path('<slug:usuarioEscuela>/cursos/<slug:nombreCurso>/', EstudianteCursoDetailView.as_view(), name='estudiante-curso-detail'),


    # CHAT ABAJO ESTUDIANTES
    path('est/<str:usuarioEscuela>/cursos/', ProfesorCursoListView.as_view()),
    path('est/<str:usuarioEscuela>/', EstudianteCursosView.as_view(), name='estudiante-cursos'),
    path('est/<str:usuarioEscuela>/cursos/<slug:slugCurso>/',EstudianteCursoDetailViewEstudiante.as_view(),name='estudiante-curso-detail'),
    path('est/<str:usuarioEscuela>/cursos/<slug:nombreCurso>/lecciones/<int:pk>/', EstudianteLeccionDetailView.as_view(),name='estudiante-leccion-detail')
]
