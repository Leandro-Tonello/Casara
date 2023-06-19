"""
Definition of models.
"""
from django.db import models
from gc import enable
from unittest.util import _MAX_LENGTH

# Create your models here.
class Registro(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    nombre_usuario = models.CharField(max_length=100)
    apellido_usuario = models.CharField(max_length=100)
    codigo_maquina = models.CharField(max_length=100)
    accion = models.CharField(max_length=100)
    descripcion = models.TextField()
    enabled = models.BooleanField()

    def str(self):
        return f"{self.id}"