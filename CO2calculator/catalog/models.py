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
    nombreUsuario=models.TextField()
    

    def __str__(self):
        return str(self.id)

class ConsumoVehiculo(models.Model):
    nombreUsuario=models.ForeignKey('TestUs',on_delete=models.SET_NULL,null=True)
    tipoVehiculo=models.TextField()
    kilometrosSemana=models.IntegerField()
    tipoCombustible=models.TextField()

    def __str__(self):
        return str(self.id)

class ConsumoEdificios(models.Model):
    nombreUsuario=models.ForeignKey('TestUs',on_delete=models.SET_NULL,null=True)
    numeroEdificios=models.IntegerField()
    tipoEdificio=models.TextField()

    def __str__(self):
        return str(self.id)

class TestUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombreUsuario = models.TextField()

    def __str__(self):
        return str(self.id)

    