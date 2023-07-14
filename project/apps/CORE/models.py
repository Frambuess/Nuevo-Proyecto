from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Marcadetarjeta(models.Model):
    marca=models.CharField(max_length=10)

    def __str__(self):
        return self.marca

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nacimiento= models.DateField(null=True) # opcional
    pais_origen_id=models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    nrotarjeta=models.IntegerField(null=True)
    marca_id=models.ForeignKey(Marcadetarjeta, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

'''

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    '''