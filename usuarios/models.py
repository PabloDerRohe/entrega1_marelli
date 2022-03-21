from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    
    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)


class Usuario(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


class Asesor(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    especialidad = models.CharField(max_length=30)
    
