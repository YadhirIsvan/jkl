from django.urls import path
from tasks.api.views import AdminTareaListCreateView, AdminTareaDetailView, EstudianteTareaListView

urlpatterns = [
    path('<str:usuarioEscuela>/cursos/<str:nombreCurso>/tareas/', AdminTareaListCreateView.as_view()),
    path('<str:usuarioEscuela>/cursos/<str:nombreCurso>/tareas/<int:pk>/', AdminTareaDetailView.as_view()),

    # estudiantes
    path('est/<str:usuarioEscuela>/cursos/<str:nombreCurso>/tareas/',EstudianteTareaListView.as_view(), name='estudiante-tareas'),    
]
