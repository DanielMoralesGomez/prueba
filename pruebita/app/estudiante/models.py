from django.db import models
from app.usuario.models import Usuario  # Importa el modelo Usuario

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)
    carrera = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.matricula}"
