from django import forms
from .models import ConsumoTotal

class ConsumoTotalForm(forms.ModelForm):

    class Meta:
        model = ConsumoTotal
        fields = ('litros',)


