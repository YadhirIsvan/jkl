from django.contrib import admin
from .models import Escuela

@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clave', 'nivel_educativo', 'municipio', 'estado', 'telefono', 'correo_electronico', 'fecha_creacion')
    search_fields = ('nombre', 'clave', 'municipio', 'estado', 'correo_electronico')
    list_filter = ('nivel_educativo', 'estado')
