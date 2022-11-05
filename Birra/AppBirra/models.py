from django.db import models


class Cerveza(models.Model):
    
    estilo = models.CharField(max_length=30)
    ibu = models.IntegerField()
    alcohol= models.IntegerField()

class Menu(models.Model):

    minutas = models.CharField(max_length=30) 
    descripcion =  models.CharField(max_length=30) 
    precio = models.IntegerField()

class Cliente(models.Model):

    nombre = models.CharField(max_length=30) 
    apellido =  models.CharField(max_length=30) 
    email = models.CharField(max_length=30)