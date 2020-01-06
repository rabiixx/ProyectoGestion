from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _ 
import datetime
from .models import ConsumoAgua,ConsumoVehiculo,ConsumoEdificios,ConsumoElectricidad,ConsumoCalefaccion,PersonalEmpresa,ViajesEmpresa,GeneracionElectricidad,TestUsuario,TablaConstantes

class TestUsuarioForm(ModelForm):
	class Meta:
		model = TestUsuario
		fields = ['nombreTest']

class TablaConstantesForm(ModelForm):
	class Meta:
		model = TablaConstantes
		fields = ['cons_agua',
		'cons_edificios_acero','cons_edificios_madera','cons_edificios_cemento',
		'cons_electricidad',
		'cons_calefaccion_gasnatural','cons_calefaccion_electrico',
		'cons_calefaccion_carbon','cons_calefaccion_gasoleo',
		'cons_personal','cons_viajes',
		'cons_generacion_panelessolares','cons_generacion_minieolica',
		'cons_compensar_españa','cons_compensar_otros']

class ConsumoAguaForm(ModelForm):
	class Meta:
		model = ConsumoAgua
		fields = ['litrosAgua']

class ConsumoVehiculoForm(ModelForm):
	class Meta:
		model = ConsumoVehiculo
		fields = ['tipoVehiculo','kilometrosSemana','tipoCombustible']

class ConsumoEdificiosForm(ModelForm):
	class Meta:
		model = ConsumoEdificios
		fields = ['numeroEdificios','tipoEdificio']

class ConsumoElectricidadForm(ModelForm):
	class Meta:
		model = ConsumoElectricidad
		fields = ['kwHora']

class ConsumoCalefaccionForm(ModelForm):
	class Meta:
		model = ConsumoCalefaccion
		fields = ['tipo', 'gasto']

class PersonalEmpresaForm(ModelForm):
	class Meta:
		model = PersonalEmpresa
		fields = ['numeroPersonal']

class ViajesEmpresaForm(ModelForm):
	class Meta:
		model = ViajesEmpresa
		fields = ['tipoVehiculo','numeroViajes', 'distanciaMedia','tipoCombustible']

class GeneracionElectricidadForm(ModelForm):
	class Meta:
		model = GeneracionElectricidad
		fields = ['cantidadGenerada', 'tipo']