
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Autenticación y cuenta
    path('account/', include('user_app.api.urls')),

    # Escuelas
    path('administrador/', include('schools.api.urls')),
    # Grupos
    path('administrador/', include('groups.api.urls')),
    # Cursos
    path('administrador/', include('courses.api.urls')),
    path('profesor/', include('courses.api.urls')),
    path('estudiante/', include('courses.api.urls')),

    # Lecciones
    path('administrador/', include('lessons.api.urls')),
    path('profesor/', include('lessons.api.urls')),
    path('estudiante/', include('lessons.api.urls')),

    # Tareas
    path('administrador/', include('tasks.api.urls')),
    path('profesor/', include('tasks.api.urls')),
    path('estudiante/', include('tasks.api.urls')),

    # otras rutas
    path('', include('schools.api.urls')),  # o como lo tengas
]
