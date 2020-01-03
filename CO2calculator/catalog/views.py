from django.shortcuts import render
from .models import Tabla
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .models import ConsumoTotal
# Create your views here.
def index(request):

    num_tabla=Tabla.objects.all().count()

    return render(request,'index.html',context={'num_tabla':num_tabla},)

class TablaListView(generic.ListView):
    model = Tabla

class TablaDetailView(generic.DetailView):
    model = Tabla

class ConsumoTotalList(generic.ListView):
    model = ConsumoTotal

def home(request):
	 return render(request, 'home.html')

def radio_buttons(request):
    return render(request, 'radio.html')

def about(request):
    return render(request, 'about.html')

def calculator(request):
    return render(request, 'calculator.html')

def agua(request):
    return render(request, 'test/agua.html')
    
def vehiculos(request):
    return render(request, 'test/vehiculos.html')


