from django.db import models

# Create your models here.

class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    terminado = models.BooleanField(default=False)

    
    def __str__(self):
        return self.titulo 