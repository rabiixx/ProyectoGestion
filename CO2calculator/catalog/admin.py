from django.contrib import admin
from .models import Tabla
from .models import ConsumoAgua,ConsumoEdificios,ConsumoVehiculo,TestUsuario
# Register your models here.

#Defin el encabezado que aparecera encima de los atributos de la clase definida en model
class TablaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'comentario', 'consumo')

admin.site.register(Tabla,TablaAdmin)

admin.site.register(ConsumoAgua)

admin.site.register(ConsumoVehiculo)

admin.site.register(ConsumoEdificios)

admin.site.register(TestUsuario)