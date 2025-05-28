from django.urls import path
from schools.api.views import AdminGrupoListCreateView, AdminGrupoUsuariosDetailView

urlpatterns = [
    path('<str:usuarioEscuela>/grupos/', AdminGrupoListCreateView.as_view()),
    path('<str:usuarioEscuela>/grupos/<str:nombre>/', AdminGrupoUsuariosDetailView.as_view()),
]
