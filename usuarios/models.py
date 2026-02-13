from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nombre 