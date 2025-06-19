from django.contrib import admin
from .models import Tarea, RecursoTarea, EntregaTarea, ArchivoEntrega, TextoEntrega

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'curso', 'fecha_entrega', 'fecha_cierre', 'calificacion_maxima', 'leccion')
    list_filter = ('tipo', 'fecha_entrega', 'fecha_cierre', 'curso')
    search_fields = ('titulo', 'descripcion')

@admin.register(RecursoTarea)
class RecursoTareaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'url', 'descripcion', 'tarea')
    list_filter = ('tipo',)
    search_fields = ('descripcion', 'url')

@admin.register(EntregaTarea)
class EntregaTareaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tarea', 'estado', 'fecha_entrega')
    list_filter = ('estado', 'fecha_entrega')
    search_fields = ('usuario__username',)

@admin.register(ArchivoEntrega)
class ArchivoEntregaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'url', 'entrega')
    list_filter = ('tipo',)
    search_fields = ('url',)

@admin.register(TextoEntrega)
class TextoEntregaAdmin(admin.ModelAdmin):
    list_display = ('respuesta', 'entrega')
    search_fields = ('respuesta',)