from django.db import models
from courses.models import Curso 

class GrupoLeccion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    orden = models.IntegerField()
    curso = models.ForeignKey('courses.Curso', on_delete=models.CASCADE)

class Leccion(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    orden = models.IntegerField()
    recurso_url = models.CharField(max_length=500)
    fecha_disponible = models.DateField()
    
    grupo_leccion = models.ForeignKey(GrupoLeccion, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)  # 🔥 Esta es la FK al curso

    def __str__(self):
        return self.titulo

class LeccionUsuario(models.Model):
    ESTADOS = [
        ('sin ver', 'Sin ver'),
        ('avanzado', 'Avanzado'),
        ('finalizado', 'Finalizado'),
    ]
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    usuario = models.ForeignKey('user_app.Account', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    porcentaje_avance = models.IntegerField()
    fecha_ultimo_avance = models.DateTimeField()

class RecursoLeccion(models.Model):
    TIPOS = [
        ('video', 'Video'),
        ('imagen', 'Imagen'),
        ('pdf', 'PDF'),
        ('audio', 'Audio'),
        ('enlace', 'Enlace'),
        ('otro', 'Otro'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS)
    url = models.CharField(max_length=500)
    descripcion = models.TextField()
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)

class EstadoRecursoLeccion(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('visto', 'Visto'),
    ]
    usuario = models.ForeignKey('user_app.Account', on_delete=models.CASCADE)
    recurso_leccion = models.ForeignKey(RecursoLeccion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_visto = models.DateTimeField()
