from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

TIPO_VEHICULO = (('Coche', 'Coche'),
              ('Avión', 'Avión'),
              ('Autobús', 'Autobús'),
              ('Barco', 'Barco'),
              ('Tren', 'Tren'))
TIPO_COMBUSTIBLE_VEHICULO= (
              ('motorGasoline', 'Gasolina'),
              ('diesel', 'Diesel'),
              ('aviationGasoline', 'aviationGasoline'),
              ('jetFuel', 'jetFuel'),)
TIPO_EDIFICIO= (
              ('Cemento', 'Cemento'),
              ('Madera', 'Madera'),
              ('Acero', 'Acero'),)
TIPO_CALEFACCION= (
              ('Gas Natural', 'Gas Natural'),
              ('Eléctrico', 'Eléctrico'),
              ('Carbón', 'Carbón'),
              ('Gasóleo', 'Gasóleo'),)
TIPO_GENERAR= (
              ('Paneles Solares', 'Paneles Solares'),
              ('Minieolica', 'Minieolica'),)

class Tabla(models.Model):

    fecha = models.DateTimeField()
    comentario = models.CharField(blank=True,max_length=300, help_text="Introduzca aqui su comentario")
    consumo = models.FloatField() 
   
    def __str__(self):
        return str(self.id)

class TestUsuario(models.Model):
    nombreTest = models.CharField(max_length=30,unique=True)
    nombreUsuario=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    co2_agua = models.FloatField(default=0)
    co2_vehiculo = models.FloatField(default=0)
    co2_edificios = models.FloatField(default=0)
    co2_electricidad = models.FloatField(default=0)
    co2_calefaccion = models.FloatField(default=0)
    co2_total = models.FloatField(default=0)

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
    tipoVehiculo=models.CharField(max_length=100,choices=TIPO_VEHICULO,default="Coche")
    kilometrosSemana=models.IntegerField()
    tipoCombustible=models.CharField(max_length=100,choices=TIPO_COMBUSTIBLE_VEHICULO,default="Gasolina")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class ConsumoEdificios(models.Model):
    nombreUsuario= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    numeroEdificios=models.IntegerField()
    tipoEdificio=models.CharField(max_length=100,choices=TIPO_EDIFICIO,default="Cemento")
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
    tipo = models.CharField(max_length=100,choices=TIPO_CALEFACCION,default="Gas Natural")
    gasto = models.IntegerField()
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
    distanciaMedia = models.IntegerField()
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class GeneracionElectricidad(models.Model):
    nombreUsuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cantidadGenerada = models.FloatField()
    tipo = models.CharField(max_length=100,choices=TIPO_GENERAR,default="Paneles Solares")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def  __str__(self):
        return str(self.id)

