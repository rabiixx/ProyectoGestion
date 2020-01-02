from django.db import models
import datetime

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

    