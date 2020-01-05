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

class TestUsuario(models.Model):
    nombreTest = models.CharField(max_length=30,unique=True)
    nombreUsuario=models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreTest)

class ConsumoAgua(models.Model):
    litrosAgua = models.IntegerField()
    nombreUsuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class ConsumoVehiculo(models.Model):
    nombreUsuario= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    tipoVehiculo=models.CharField(max_length=20, help_text="(Vehículos dedicados a transporte)")
    kilometrosSemana=models.IntegerField()
    tipoCombustible=models.CharField(max_length=20, help_text="(Vehículos dedicados a transporte)")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class ConsumoEdificios(models.Model):
    nombreUsuario= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    numeroEdificios=models.IntegerField()
    tipoEdificio=models.TextField()
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class ConsumoElectricidad(models.Model):
    nombreUsuario= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    kwHora=models.FloatField()
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class ConsumoCalefaccion(models.Model):
    nombreUsuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, help_text="(Tipo de combustible para la calefaccion)")
    gasto = models.FloatField()
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class PersonalEmpresa(models.Model):
    nombreUsuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    numeroPersonal = models.IntegerField()
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class ViajesEmpresa(models.Model):
    nombreUsuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    numeroViajes = models.IntegerField()
    distanciaMedia = models.FloatField()
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class GeneracionElectricidad(models.Model):
    nombreUsuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cantidadGenerada = models.FloatField()
    tipo = models.CharField(max_length=20, help_text="(Tipo de instalaciones de generacion de electricidad)")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def  __str__(self):
        return str(self.id)

