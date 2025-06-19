from django.db import models
from django.utils.text import slugify


class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    id_docente = models.ForeignKey('user_app.Account', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)
    tipo_curso = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    escuela = models.ForeignKey('schools.Escuela', on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class HorarioCurso(models.Model):
    DIAS = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

class CursoGrupo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    grupo = models.ForeignKey('groups.Grupo', on_delete=models.CASCADE)

class CursoUsuario(models.Model):
    ESTADOS = [
        ('inscrito', 'Inscrito'),
        ('aprobado', 'Aprobado'),
        ('reprobado', 'Reprobado'),
        ('retirado', 'Retirado'),
    ]
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuario = models.ForeignKey('user_app.Account', on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
