from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Mediodepago(models.Model):
    marca=models.CharField(max_length=25)

    def __str__(self):
        return self.marca

class Cliente(models.Model):
    pais_origen_id=models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    apellido=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    nacimiento= models.DateField(null=True) # opcional
    marca_id=models.ForeignKey(Mediodepago, on_delete=models.SET_NULL, null=True)
    nrotarjeta=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}. Nació el {self.nacimiento}. Su tarjeta es {self.marca_id} nro {self.nrotarjeta}"