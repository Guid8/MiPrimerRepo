from django.db import models

class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada=models.CharField(max_length=40)

class Primo(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.CharField(max_length=40)

class Tio(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.CharField(max_length=40)
    

class Abuelo(models.Model):

    nombre=models.CharField(max_length=30)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
