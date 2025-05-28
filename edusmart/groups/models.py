from django.db import models

class Grupo(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_creacion = models.DateField()
    activo = models.BooleanField(default=True)
    escuela = models.ForeignKey('schools.Escuela', on_delete=models.CASCADE)

class GrupoUsuario(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    usuario = models.ForeignKey('user_app.Account', on_delete=models.CASCADE)
