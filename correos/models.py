from django.db import models

class Correo(models.Model):
    asunto = models.CharField(max_length=255, blank=True)
    cuerpo = models.TextField(blank=True)
    categoria = models.CharField(max_length=20,
        choices=[
            ('pqr', 'PQR'),
            ('demanda', 'Demanda'),
            ('tutela', 'Tutela'),
            ('ninguno', 'Ninguno')
        ])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.correo_id} - {self.categoria}"