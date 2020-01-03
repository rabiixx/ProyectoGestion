from django.shortcuts import render
from django.shortcuts import redirect
from .models import Tabla
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
import json
from urllib.request import urlopen
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from .forms import ConsumoAguaForm
# Create your views here.
def index(request):

    num_tabla=Tabla.objects.all().count()

    return render(request,'index.html',context={'num_tabla':num_tabla},)

class TablaListView(generic.ListView):
    model = Tabla

class TablaDetailView(generic.DetailView):
    model = Tabla

def testUs(request):
     return render(request, '')

def home(request):
	 return render(request, 'home.html')

def radio_buttons(request):
    return render(request, 'radio.html')

def about(request):
    return render(request, 'about.html')

def calculator(request):
    if request.user.is_authenticated: 
        return render(request, 'calculator.html')
    else:
        return redirect('login')

def agua(request):
    form=ConsumoAguaForm()
     # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = ConsumoAguaForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('../vehiculos')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'test/agua.html', {'form': form})
    
def vehiculos(request):
    return render(request, 'test/vehiculos.html')
   

def edificios(request):
    return render(request, 'test/edificios.html')

def consumoElectricidad(request):
    return render(request, 'test/consumoElectricidad.html')

def calefaccion(request):
    return render(request, 'test/calefaccion.html')

def personal(request):
    return render(request, 'test/personal.html')

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('home')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})

def login(request):
     # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('home')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('home')
