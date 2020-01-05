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
from .models import ConsumoAgua,ConsumoVehiculo,ConsumoEdificios,ConsumoElectricidad,ConsumoCalefaccion,PersonalEmpresa,ViajesEmpresa,GeneracionElectricidad,TestUsuario
from .forms import ConsumoAguaForm,ConsumoVehiculoForm,ConsumoEdificiosForm,ConsumoElectricidadForm,ConsumoCalefaccionForm,PersonalEmpresaForm,ViajesEmpresaForm,GeneracionElectricidadForm,TestUsuarioForm
# Create your views here.
def index(request):

    num_tabla=Tabla.objects.all().count()

    return render(request,'index.html',context={'num_tabla':num_tabla},)

class TablaListView(generic.ListView):
    model = Tabla

class TablaDetailView(generic.DetailView):
    model = Tabla

def resultado(request,nombreTest_id):
    context={
        'url': nombreTest_id,
    }
    return render(request, 'test/resultado.html', context)

def vehiculospregunta(request,nombreTest_id):
    context={
        'url': nombreTest_id,
    }
    return render(request, 'test/vehiculospregunta.html', context)

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

def test(request):
    form=TestUsuarioForm()
     # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = TestUsuarioForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.nombreUsuario = request.user
            instancia.save()

            return redirect('../agua/'+instancia.nombreTest)
    # Si llegamos al final renderizamos el formulario
    return render(request, 'test/test.html', {'form': form})

def agua(request,nombreTest_id):
    form=ConsumoAguaForm()
     # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = ConsumoAguaForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            instancia = form.save(commit=False)
            auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
            instancia.nombreTest=auxiliar
            print(auxiliar)
            instancia.nombreUsuario = request.user
            instancia.save()
            return redirect('../../vehiculos/'+nombreTest_id)
    # Si llegamos al final renderizamos el formulario
    return render(request, 'test/agua.html', {'form': form})
    
def vehiculos(request,nombreTest_id):
    form=ConsumoVehiculoForm()
     # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = ConsumoVehiculoForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            instancia = form.save(commit=False)
            auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
            instancia.nombreTest=auxiliar
            instancia.nombreUsuario = request.user
            instancia.save()
            return redirect('../../vehiculospregunta/'+nombreTest_id)
    # Si llegamos al final renderizamos el formulario
    return render(request, 'test/vehiculos.html', {'form': form})
   

def edificios(request,nombreTest_id):
    form = ConsumoEdificiosForm()
    if request.method == 'POST':
        form=ConsumoEdificiosForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
            instancia.nombreTest=auxiliar
            instancia.nombreUsuario = request.user
            instancia.save()
            return redirect('../../consumoElectricidad/'+nombreTest_id)
    return render(request, 'test/edificios.html', {'form': form})

def consumoElectricidad(request,nombreTest_id):
    form = ConsumoElectricidadForm()
    if request.method  == 'POST':
        form=ConsumoElectricidadForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
            instancia.nombreTest=auxiliar
            instancia.nombreUsuario = request.user
            instancia.save()
            return redirect('../../calefaccion/'+nombreTest_id)
    return render(request, 'test/consumoElectricidad.html', {'form': form})

def calefaccion(request,nombreTest_id):
    form = ConsumoCalefaccionForm()
    if request.method == 'POST':
        form=ConsumoCalefaccionForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
            instancia.nombreTest=auxiliar
            instancia.nombreUsuario = request.user
            instancia.save()
            return redirect('../../personal/'+nombreTest_id)
    return render(request, 'test/calefaccion.html', {'form': form})

def personal(request,nombreTest_id):
    form = PersonalEmpresaForm()
    if request.method == 'POST':
        form=PersonalEmpresaForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
            instancia.nombreTest=auxiliar
            instancia.nombreUsuario = request.user
            instancia.save()
            return redirect('../../viajes/'+nombreTest_id)
    return render(request, 'test/personal.html', {'form': form})

def viajes(request,nombreTest_id):
    form = ViajesEmpresaForm()
    if request.method == 'POST':
        form=ViajesEmpresaForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
            instancia.nombreTest=auxiliar
            instancia.nombreUsuario = request.user
            instancia.save()
            return redirect('../../generacionElectricidad/'+nombreTest_id)
    return render(request, 'test/viajes.html', {'form': form})

def generacionElectricidad(request,nombreTest_id):
    form = GeneracionElectricidadForm()
    if request.method == 'POST':
        form=GeneracionElectricidadForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
            instancia.nombreTest=auxiliar
            instancia.nombreUsuario = request.user
            instancia.save()
            return redirect('../../resultado/'+nombreTest_id)
    return render(request, 'test/generarElectricidad.html', {'form': form})

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
                return redirect('calculator')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('home')

def cuenta(request):
    if request.user.is_authenticated:
        context={
       'num_Agua':ConsumoAgua.objects.filter(nombreUsuario=request.user).count(),
        'num_ConsumoVehiculo':ConsumoVehiculo.objects.filter(nombreUsuario=request.user).count(),
        'num_ConsumoEdificios':ConsumoEdificios.objects.filter(nombreUsuario=request.user).count(),
        'num_ConsumoElectricidad':ConsumoElectricidad.objects.filter(nombreUsuario=request.user).count(),
        'num_ConsumoCalefaccion':ConsumoCalefaccion.objects.filter(nombreUsuario=request.user).count(),
        'num_PersonalEmpresa':PersonalEmpresa.objects.filter(nombreUsuario=request.user).count(),
        'num_ViajesEmpresa':ViajesEmpresa.objects.filter(nombreUsuario=request.user).count(),
        'num_GeneracionElectricidad':GeneracionElectricidad.objects.filter(nombreUsuario=request.user).count(),
        }
        return render(request,'cuenta.html', context)
    else:
        return redirect('login')


class AguaListView(generic.ListView):
    model = ConsumoAgua
