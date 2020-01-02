from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from .models import ConsumoTotal

class ConsumoTotalForm(forms.ModelForm):

    class Meta:
        model = ConsumoTotal
        fields = ('litros',)
