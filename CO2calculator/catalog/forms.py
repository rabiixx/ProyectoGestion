from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _ 
import datetime
from .models import ConsumoAgua,ConsumoVehiculo,ConsumoEdificios,ConsumoElectricidad,ConsumoCalefaccion,PersonalEmpresa,ViajesEmpresa,GeneracionElectricidad,TestUsuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TestUsuarioForm(ModelForm):
	class Meta:
		model = TestUsuario
		fields = ['nombreTest']

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
		fields = ['numeroViajes', 'distanciaMedia']

class GeneracionElectricidadForm(ModelForm):
	class Meta:
		model = GeneracionElectricidad
		fields = ['cantidadGenerada', 'tipo']
