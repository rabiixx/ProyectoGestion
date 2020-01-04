from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class Tabla(models.Model):

    fecha = models.DateTimeField()
    comentario = models.CharField(blank=True,max_length=300, help_text="Introduzca aqui su comentario")
    consumo = models.FloatField() 
   
    def __str__(self):
        return str(self.id)

class ConsumoAgua(models.Model):
    litrosAgua = models.IntegerField()
    nombreUsuario=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)

class ConsumoVehiculo(models.Model):
    nombreUsuario= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    tipoVehiculo=models.CharField(max_length=20, help_text="(Vehículos dedicados a transporte)")
    kilometrosSemana=models.IntegerField()
    tipoCombustible=models.CharField(max_length=20, help_text="(Vehículos dedicados a transporte)")

    def __str__(self):
        return str(self.id)

class ConsumoEdificios(models.Model):
    nombreUsuario= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    numeroEdificios=models.IntegerField()
    tipoEdificio=models.TextField()

    def __str__(self):
        return str(self.id)

    