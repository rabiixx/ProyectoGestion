from django.contrib import admin
from .models import ConsumoAgua,ConsumoEdificios,ConsumoVehiculo,TestUsuario,ConsumoElectricidad,PersonalEmpresa,ConsumoCalefaccion,ViajesEmpresa,GeneracionElectricidad, TablaConstantes
# Register your models here.

#Defin el encabezado que aparecera encima de los atributos de la clase definida en model
class TablaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'comentario', 'consumo')


admin.site.register(ConsumoAgua)

admin.site.register(ConsumoVehiculo)

admin.site.register(ConsumoEdificios)

admin.site.register(ConsumoElectricidad)

admin.site.register(ConsumoCalefaccion)

admin.site.register(PersonalEmpresa)

admin.site.register(ViajesEmpresa)

admin.site.register(GeneracionElectricidad)

admin.site.register(TestUsuario)

admin.site.register(TablaConstantes)