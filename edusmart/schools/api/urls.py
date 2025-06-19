from django.urls import path
from schools.api import views
from .views import EscuelaCreateView, EscuelasDelProfesorView, EscuelasDelEstudianteView,EstudianteEscuelasView

urlpatterns = [
    path('escuelas/', EscuelaCreateView.as_view(), name='escuela-create'),
    path('<str:usuarioEscuela>/informacion/', views.EscuelaDetailView.as_view()),
    path('profesor/', EscuelasDelProfesorView.as_view(), name='escuelas-del-profesor'),
    path('estudiante/', EscuelasDelEstudianteView.as_view(), name='escuelas-del-estudiante'),

    # path que nos permite mostrarnos los cursos en los que esta un estudiante
    path('estudiante/<str:usuarioEscuela>/', EstudianteEscuelasView.as_view(), name='estudiante-escuelas'),

]
