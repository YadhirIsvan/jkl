from django.contrib import admin
from user_app.models import Account, UsuarioEscuela

# Register your models here.
admin.site.register(Account)
admin.site.register(UsuarioEscuela)

class UsuarioEscuelaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'escuela', 'rol', 'fecha_asignacion')
    search_fields = ('usuario__email', 'usuario__username', 'escuela__nombre')
    list_filter = ('rol', 'fecha_asignacion')
    ordering = ('-fecha_asignacion',)