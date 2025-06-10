from django.db import models
from django.conf import settings


class Escuela(models.Model):
    nombre = models.CharField(max_length=255)
    clave = models.CharField(max_length=50)
    nivel_educativo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.CharField(max_length=100)
    director = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='escuelas_dirigidas'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

