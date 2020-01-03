from django.contrib import admin
from .models import Tabla
from .models import ConsumoAgua
# Register your models here.

#Defin el encabezado que aparecera encima de los atributos de la clase definida en model
class TablaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'comentario', 'consumo')

admin.site.register(Tabla,TablaAdmin)

admin.site.register(ConsumoAgua)