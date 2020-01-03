from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from .models import ConsumoAgua,ConsumoVehiculo,ConsumoEdificios

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