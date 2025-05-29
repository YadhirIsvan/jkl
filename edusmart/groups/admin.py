from django.contrib import admin
from .models import Grupo, GrupoUsuario

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion', 'activo', 'escuela')
    list_filter = ('activo', 'fecha_creacion', 'escuela')
    search_fields = ('nombre',)

@admin.register(GrupoUsuario)
class GrupoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'usuario')
    search_fields = ('grupo__nombre', 'usuario__username')  # Asumiendo que Account tiene username
    list_filter = ('grupo',)
