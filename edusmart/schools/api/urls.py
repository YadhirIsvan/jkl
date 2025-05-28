from django.urls import path
from schools.api import views

urlpatterns = [
    path('<str:usuarioEscuela>/informacion/', views.EscuelaDetailView.as_view()),
]