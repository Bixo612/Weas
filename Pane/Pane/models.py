from django.db import models

class Taller(models.Model):
    rol             = models.CharField(primary_key=True, max_length=10)
    razon_social    = models.CharField(max_length=100)
    direccion       = models.CharField(max_length=200)
    comuna          = models.CharField(max_length=100)
    telefono        = models.CharField(max_length=20)
    email           = models.EmailField()

class Cliente(models.Model):
    nick    = models.CharField(max_length=100, primary_key=True)
    email   = models.EmailField()
    clave   = models.CharField(max_length=100)
    patente = models.CharField(max_length=10)

class Comentario(models.Model):
    id          = models.AutoField(primary_key=True)
    fecha       = models.DateField()
    comentario  = models.TextField()
    nota        = models.IntegerField()
    taller      = models.ForeignKey(Taller, on_delete=models.CASCADE)
    cliente     = models.ForeignKey(Cliente, on_delete=models.CASCADE)