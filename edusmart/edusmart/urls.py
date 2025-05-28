"""
URL configuration for edusmart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
]
