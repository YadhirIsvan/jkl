from django.contrib import admin
from .models import Curso, HorarioCurso, CursoGrupo, CursoUsuario

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'id_docente', 'fecha_inicio', 'fecha_fin', 'activo', 'tipo_curso', 'escuela')
    list_filter = ('activo', 'tipo_curso', 'fecha_inicio', 'fecha_fin', 'escuela')
    search_fields = ('nombre', 'codigo', 'descripcion')

@admin.register(HorarioCurso)
class HorarioCursoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'dia_semana', 'hora_inicio', 'hora_fin')
    list_filter = ('dia_semana', 'curso')
    search_fields = ('curso__nombre',)

@admin.register(CursoGrupo)
class CursoGrupoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'grupo')
    list_filter = ('curso', 'grupo')
    search_fields = ('curso__nombre', 'grupo__nombre')

@admin.register(CursoUsuario)
class CursoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('curso', 'usuario', 'fecha_inscripcion', 'estado')
    list_filter = ('estado', 'fecha_inscripcion')
    search_fields = ('usuario__username', 'curso__nombre')
