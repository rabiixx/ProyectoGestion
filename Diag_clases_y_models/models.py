from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

TIPO_VEHICULO = (('anyCar', 'Coche'),
              ('anyFlight', 'Avión'),
              ('bus', 'Autobús'),
              ('taxi', 'Taxi'),
              ('transitRail', 'Tren'),
              ('motorbike', 'Moto'))
TIPO_COMBUSTIBLE_VEHICULO= (
              ('motorGasoline', 'Gasolina'),
              ('diesel', 'Diesel'),
              ('aviationGasoline', 'Gasolina Aviacion'),
              ('jetFuel', 'Jet Fuel'),)
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

class TablaConstantes(models.Model):
    nombreUsuario=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cons_agua = models.FloatField(default=1.5)
    cons_edificios_acero = models.FloatField(default=1.5)
    cons_edificios_madera = models.FloatField(default=1.5)
    cons_edificios_cemento = models.FloatField(default=1.5)
    cons_electricidad = models.FloatField(default=1.5)
    cons_calefaccion_gasnatural = models.FloatField(default=1.5)
    cons_calefaccion_electrico = models.FloatField(default=1.5)
    cons_calefaccion_carbon = models.FloatField(default=1.5)
    cons_calefaccion_gasoleo = models.FloatField(default=1.5)
    cons_personal = models.FloatField(default=1.5)
    cons_viajes = models.FloatField(default=1.5)
    cons_generacion_panelessolares = models.FloatField(default=1.5)
    cons_generacion_minieolica = models.FloatField(default=1.5)
    cons_compensar_españa = models.FloatField(default=0.05)
    cons_compensar_otros = models.FloatField(default=0.008)

    def __str__(self):
        return str(self.id)


class TestUsuario(models.Model):
    nombreTest = models.CharField("Nombre del test",max_length=30,unique=True)
    nombreUsuario=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    co2_agua = models.FloatField(default=0)
    co2_vehiculo = models.FloatField(default=0)
    co2_edificios = models.FloatField(default=0)
    co2_electricidad = models.FloatField(default=0)
    co2_calefaccion = models.FloatField(default=0)
    co2_personal = models.FloatField(default=0)
    co2_viajes = models.FloatField(default=0)
    co2_generacion = models.FloatField(default=0)
    co2_total = models.FloatField(default=0)

    def __str__(self):
        return str(self.nombreTest)



class ConsumoAgua(models.Model):
    litrosAgua = models.IntegerField("Litros de agua",help_text="(anual)")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class ConsumoVehiculo(models.Model):
    tipoVehiculo=models.CharField("Tipo de vehículo",max_length=100,choices=TIPO_VEHICULO,default="Coche")
    kilometrosSemana=models.IntegerField("Kilómetros recorridos anualmente",help_text="(suma de todos los vehículos de ese tipo)")
    tipoCombustible=models.CharField("Combustible usado",max_length=100,choices=TIPO_COMBUSTIBLE_VEHICULO,default="Gasolina")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class ConsumoEdificios(models.Model):
    numeroEdificios=models.IntegerField("Numero de edificios")
    tipoEdificio=models.CharField("Material de construcción",max_length=100,choices=TIPO_EDIFICIO,default="Cemento")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class ConsumoElectricidad(models.Model):
    kwHora=models.FloatField("Consumo eléctrico",help_text="Kilowatios/año")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class ConsumoCalefaccion(models.Model):
    tipo = models.CharField("Tipo de Combustible",max_length=100,choices=TIPO_CALEFACCION,default="Gas Natural")
    gasto = models.IntegerField("Gasto generado",help_text="(anual)")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class PersonalEmpresa(models.Model):
    numeroPersonal = models.IntegerField("Numero de personal")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class ViajesEmpresa(models.Model):
    tipoVehiculo=models.CharField(max_length=100,choices=TIPO_VEHICULO,default="Coche")
    numeroViajes = models.IntegerField("Numero de viajes al año")
    distanciaMedia = models.IntegerField("Distancia media (km)")
    tipoCombustible=models.CharField("Tipo de combustible",max_length=100,choices=TIPO_COMBUSTIBLE_VEHICULO,default="Gasolina")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class GeneracionElectricidad(models.Model):
    cantidadGenerada = models.FloatField("Cantidad de energía generada ",help_text="(kw/año)")
    tipo = models.CharField("Tipo de energía generada",max_length=100,choices=TIPO_GENERAR,default="Paneles Solares")
    nombreTest=models.ForeignKey('TestUsuario',on_delete=models.CASCADE)

    def  __str__(self):
        return str(self.id)

