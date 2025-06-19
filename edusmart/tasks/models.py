from django.db import models
from courses.models import Curso  

class Tarea(models.Model):
    TIPOS = [
        ('archivo', 'Archivo'),
        ('texto', 'Texto'),
        ('quiz', 'Quiz'),
    ]
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS)
    fecha_entrega = models.DateField()
    fecha_cierre = models.DateField()
    calificacion_maxima = models.DecimalField(max_digits=5, decimal_places=2)
    leccion = models.ForeignKey('lessons.Leccion', on_delete=models.CASCADE)
    curso = models.ForeignKey('courses.Curso', on_delete=models.CASCADE, null=True, blank=True)



class RecursoTarea(models.Model):
    TIPOS = [
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('imagen', 'Imagen'),
        ('enlace', 'Enlace'),
        ('otro', 'Otro'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS)
    url = models.CharField(max_length=500)
    descripcion = models.TextField()
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)

class EntregaTarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('entregada', 'Entregada'),
        ('evaluada', 'Evaluada'),
    ]
    usuario = models.ForeignKey('user_app.Account', on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_entrega = models.DateTimeField(auto_now_add=True)

class ArchivoEntrega(models.Model):
    TIPOS = [
        ('pdf', 'PDF'),
        ('imagen', 'Imagen'),
        ('video', 'Video'),
        ('documento', 'Documento'),
        ('otro', 'Otro'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS)
    url = models.CharField(max_length=500)
    entrega = models.ForeignKey(EntregaTarea, on_delete=models.CASCADE)

class TextoEntrega(models.Model):
    respuesta = models.TextField()
    entrega = models.ForeignKey(EntregaTarea, on_delete=models.CASCADE)
