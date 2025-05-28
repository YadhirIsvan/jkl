from django.db import models

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
    director = models.IntegerField()  # puedes hacer FK al modelo Account si quieres
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
