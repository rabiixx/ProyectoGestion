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
    usuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    litrosAgua = models.FloatField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.id


    