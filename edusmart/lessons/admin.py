from django.contrib import admin
from .models import GrupoLeccion, Leccion, LeccionUsuario, RecursoLeccion, EstadoRecursoLeccion

@admin.register(GrupoLeccion)
class GrupoLeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'curso')
    list_filter = ('curso',)
    search_fields = ('titulo', 'descripcion')

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'fecha_disponible', 'grupo_leccion', 'curso')
    list_filter = ('fecha_disponible', 'grupo_leccion', 'curso')
    search_fields = ('titulo', 'contenido', 'curso__nombre')

@admin.register(LeccionUsuario)
class LeccionUsuarioAdmin(admin.ModelAdmin):
    list_display = ('leccion', 'usuario', 'estado', 'porcentaje_avance', 'fecha_ultimo_avance')
    list_filter = ('estado',)
    search_fields = ('usuario__username', 'leccion__titulo')

@admin.register(RecursoLeccion)
class RecursoLeccionAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'url', 'leccion', 'fecha_subida')
    list_filter = ('tipo', 'fecha_subida')
    search_fields = ('descripcion', 'url')

@admin.register(EstadoRecursoLeccion)
class EstadoRecursoLeccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'recurso_leccion', 'estado', 'fecha_visto')
    list_filter = ('estado',)
    search_fields = ('usuario__username', 'recurso_leccion__descripcion')
