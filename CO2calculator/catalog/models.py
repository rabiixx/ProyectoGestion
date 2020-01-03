from django.db import models
from django.utils import timezone

class Tabla(models.Model):
    """
    Modelo que representa la produccion de CO2 en centimetros cubicos  
    """
    fecha = models.DateTimeField()
    comentario = models.CharField(blank=True,max_length=300, help_text="Introduzca aqui su comentario")
    consumo = models.FloatField() 
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return str(self.id)
class ConsumoTotal(models.Model):
    email=models.EmailField()
    litrosAgua = models.FloatField(max_length=200)
    numeroEdificios=models.IntegerField()
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.email

# Tabla de Factores de Emision
class FactorEmision(models.Model):
    combustible = models.CharField(max_length = 35)
    factor_emision = models.FloatField()
    created_date = models.DateTimeField()
    unidad_fe = models.CharField(max_length = 10, default='kgCO2/l')

    def __str__(self):
        cadena = "{0}   {1}"
        return cadena.format(self.combustible, self.factor_emision);