from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()