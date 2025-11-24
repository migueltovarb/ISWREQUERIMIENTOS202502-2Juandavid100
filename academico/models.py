from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    ROLES = (
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
        ('admin', 'Administrador'),
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.IntegerField(default=3)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
