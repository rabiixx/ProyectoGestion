from django.shortcuts import render
from django.shortcuts import redirect
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
from .models import ConsumoAgua,ConsumoVehiculo,ConsumoEdificios,ConsumoElectricidad,ConsumoCalefaccion,PersonalEmpresa,ViajesEmpresa,GeneracionElectricidad,TestUsuario, TablaConstantes
from .forms import ConsumoAguaForm,ConsumoVehiculoForm,ConsumoEdificiosForm,ConsumoElectricidadForm,ConsumoCalefaccionForm,PersonalEmpresaForm,ViajesEmpresaForm,GeneracionElectricidadForm,TestUsuarioForm, TablaConstantesForm

"""  PRIMERA PAGINA DE TODAS   """

def index(request):
    return redirect('home') 
    
"""
<---------------------------------------------------------------------------------------------->
<---------------------------------------------------------------------------------------------->
<---------------------VISTAS DE LAS TABLAS EN LA CUENTA DEL USUARIO----------------------------> 
<---------------------------------------------------------------------------------------------->
<---------------------------------------------------------------------------------------------->
"""

class TestUsuarioListView(generic.ListView):
    template_name = 'cuenta/testusuario_list.html'
    def get_queryset(self):
        queryset = TestUsuario.objects.filter(nombreUsuario__username=self.kwargs['nombre'])
        return queryset

def TestDetallado(request,nomtest):
    test=TestUsuario.objects.get(nombreTest=nomtest)
    consumoAgua=ConsumoAgua.objects.get(nombreTest=test)
    consumoElectricidad=ConsumoElectricidad.objects.get(nombreTest=test)
    consumoEdificios=ConsumoEdificios.objects.get(nombreTest=test)
    consumoCalefaccion=ConsumoCalefaccion.objects.get(nombreTest=test)
    personalEmpresa=PersonalEmpresa.objects.get(nombreTest=test)
    generacionElectricidad=GeneracionElectricidad.objects.get(nombreTest=test)
    context={
    'pk_agua':consumoAgua.id,
    'pk_electricidad':consumoElectricidad.id,
    'pk_edificios':consumoEdificios.id,
    'pk_calefaccion':consumoCalefaccion.id,
    'pk_personal':personalEmpresa.id,
    'pk_generacion':generacionElectricidad.id,
    'nomtest':nomtest,}
    return render(request, 'testdetallado.html', context)

""" <-------------------------------CONSUMO DE AGUA----------------------------------------------> """

class ConsumoAguaDetailView(generic.DetailView):
    model = ConsumoAgua
    template_name = 'cuenta/consumoagua_detail.html'

def ConsumoAguaModify(request,pk):
    form=ConsumoAguaForm()
    if request.method == "POST":
        form = ConsumoAguaForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            ConsumoAgua.objects.filter(id=pk).update(litrosAgua=instancia.litrosAgua)
            return redirect('../ConsumoAguaDetail/'+ pk)
    return render(request, 'cuenta/consumoaguamodify.html',{'form': form})

""" <-------------------------------CONSUMO DE VEHICULOS----------------------------------------------> """

class ConsumoVehiculoListView(generic.ListView):
    template_name = 'cuenta/consumovehiculo_list.html'
    def get_queryset(self):
        queryset = ConsumoVehiculo.objects.filter(nombreTest__nombreTest=self.kwargs['nomtest'])
        return queryset

class ConsumoVehiculoDetailView(generic.DetailView):
    model = ConsumoVehiculo
    template_name = 'cuenta/consumovehiculo_detail.html'

def ConsumoVehiculoModify(request,pk):
    form=ConsumoVehiculoForm()
    if request.method == "POST":
        form = ConsumoVehiculoForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            ConsumoVehiculo.objects.filter(id=pk).update(tipoVehiculo=instancia.tipoVehiculo,kilometrosSemana=instancia.kilometrosSemana,tipoCombustible=instancia.tipoCombustible)
            return redirect('../ConsumoVehiculoDetail/'+ pk)
    return render(request, 'cuenta/consumovehiculomodify.html',{'form': form})

""" <-----------------------------------CONSUMO DE EDIFICIOS----------------------------------------------> """
class ConsumoEdificiosDetailView(generic.DetailView):
    model = ConsumoEdificios
    template_name = 'cuenta/consumoedificios_detail.html'

def ConsumoEdificiosModify(request,pk):
    form=ConsumoEdificiosForm()
    if request.method == "POST":
        form = ConsumoEdificiosForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            ConsumoEdificios.objects.filter(id=pk).update(numeroEdificios=instancia.numeroEdificios,tipoEdificio=instancia.tipoEdificio)
            return redirect('../ConsumoEdificiosDetail/'+ pk)
    return render(request, 'cuenta/consumoedificiosmodify.html',{'form': form})

""" <--------------------------------CONSUMO DE ELECTRICIDAD----------------------------------------------> """

class ConsumoElectricidadDetailView(generic.DetailView):
    model = ConsumoElectricidad
    template_name = 'cuenta/consumoelectricidad_detail.html'

def ConsumoElectricidadModify(request,pk):
    form=ConsumoElectricidadForm()
    if request.method == "POST":
        form = ConsumoElectricidadForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            ConsumoElectricidad.objects.filter(id=pk).update(kwHora=instancia.kwHora)
            return redirect('../ConsumoElectricidadDetail/'+ pk)
    return render(request, 'cuenta/consumoelectricidadmodify.html',{'form': form})

""" <---------------------------------CONSUMO DE CALEFACCION----------------------------------------------> """

class ConsumoCalefaccionDetailView(generic.DetailView):
    model = ConsumoCalefaccion
    template_name = 'cuenta/consumocalefaccion_detail.html'

def ConsumoCalefaccionModify(request,pk):
    form=ConsumoCalefaccionForm()
    if request.method == "POST":
        form = ConsumoCalefaccionForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            ConsumoCalefaccion.objects.filter(id=pk).update(tipo=instancia.tipo, gasto=instancia.gasto)
            return redirect('../ConsumoCalefaccionDetail/'+ pk)
    return render(request, 'cuenta/consumocalefaccionmodify.html',{'form': form})
""" <------------------------------------CONSUMO DE PERSONAL----------------------------------------------> """

class PersonalEmpresaDetailView(generic.DetailView):
    model = PersonalEmpresa
    template_name = 'cuenta/personalempresa_detail.html'

def PersonalEmpresaModify(request,pk):
    form=PersonalEmpresaForm()
    if request.method == "POST":
        form = PersonalEmpresaForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            PersonalEmpresa.objects.filter(id=pk).update(numeroPersonal=instancia.numeroPersonal)
            return redirect('../PersonalEmpresaDetail/'+ pk)
    return render(request, 'cuenta/personalempresamodify.html',{'form': form})
""" <--------------------------------------CONSUMO DE VIAJES----------------------------------------------> """

class ViajesEmpresaListView(generic.ListView):
    template_name = 'cuenta/viajesempresa_list.html'
    def get_queryset(self):
        queryset = ViajesEmpresa.objects.filter(nombreTest__nombreTest=self.kwargs['nomtest'])
        return queryset

class ViajesEmpresaDetailView(generic.DetailView):
    model = ViajesEmpresa
    template_name = 'cuenta/viajesempresa_detail.html'

def ViajesEmpresaModify(request,pk):
    form=ViajesEmpresaForm()
    if request.method == "POST":
        form = ViajesEmpresaForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            ViajesEmpresa.objects.filter(id=pk).update(tipoVehiculo=instancia.tipoVehiculo,numeroViajes=instancia.numeroViajes, distanciaMedia=instancia.distanciaMedia,tipoCombustible=instancia.tipoCombustible)
            return redirect('../ViajesEmpresaDetail/'+ pk)
    return render(request, 'cuenta/viajesempresamodify.html',{'form': form})

""" <----------------------------------GENERACION ELECTRICIDAD----------------------------------------------> """

class GeneracionElectricidadDetailView(generic.DetailView):
    model = GeneracionElectricidad
    template_name = 'cuenta/generacionelectricidad_detail.html'

def GeneracionElectricidadModify(request,pk):
    form=GeneracionElectricidadForm()
    if request.method == "POST":
        form = GeneracionElectricidadForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            GeneracionElectricidad.objects.filter(id=pk).update(cantidadGenerada=instancia.cantidadGenerada, tipo=instancia.tipo)
            return redirect('../GeneracionElectricidadDetail/'+ pk)
    return render(request, 'cuenta/generacionelectricidadmodify.html',{'form': form})

""" 
<---------------------------------------------------------------------------------------------->
<---------------------------------------------------------------------------------------------->
<------------------------------------VISTAS DEL TEST-------------------------------------------> 
<---------------------------------------------------------------------------------------------->
<---------------------------------------------------------------------------------------------->
"""

def resultado(request,nombreTest_id):
    auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
    agua=ConsumoAgua.objects.get(nombreTest__nombreTest=nombreTest_id)
    edificio=ConsumoEdificios.objects.get(nombreTest__nombreTest=nombreTest_id)
    electricidad=ConsumoElectricidad.objects.get(nombreTest__nombreTest=nombreTest_id)
    calefaccion=ConsumoCalefaccion.objects.get(nombreTest__nombreTest=nombreTest_id)
    personal=PersonalEmpresa.objects.get(nombreTest__nombreTest=nombreTest_id)
    generacion=GeneracionElectricidad.objects.get(nombreTest__nombreTest=nombreTest_id)
    tablacons=TablaConstantes.objects.get(nombreUsuario=request.user)


#Consumo de agua
    auxiliar.co2_agua=agua.litrosAgua*tablacons.cons_agua
#Consumo de edificios
    if edificio.tipoEdificio=='Madera':
        auxiliar.co2_edificios=edificio.numeroEdificios*tablacons.cons_edificios_madera
    elif edificio.tipoEdificio=='Acero':
        auxiliar.co2_edificios=edificio.numeroEdificios*tablacons.cons_edificios_acero
    elif edificio.tipoEdificio=='Cemento':
        auxiliar.co2_edificios=edificio.numeroEdificios*tablacons.cons_edificios_cemento
#Consumo de electricidad
    auxiliar.co2_electricidad=electricidad.kwHora*tablacons.cons_electricidad
#Consumo de calefaccion
    if calefaccion.tipo=='Gas Natural':
        auxiliar.co2_calefaccion=calefaccion.gasto*tablacons.cons_calefaccion_gasnatural
    elif calefaccion.tipo=='Eléctrico':
        auxiliar.co2_calefaccion=calefaccion.gasto*tablacons.cons_calefaccion_electrico
    elif calefaccion.tipo=='Carbón':
        auxiliar.co2_calefaccion=calefaccion.gasto*tablacons.cons_calefaccion_carbon
    elif calefaccion.tipo=='Gasóleo':
        auxiliar.co2_calefaccion=calefaccion.gasto*tablacons.cons_calefaccion_gasoleo
#Personal de empresa
    auxiliar.co2_personal=personal.numeroPersonal*tablacons.cons_personal
#Generacion de electricidad
    if generacion.tipo=='Paneles Solares':
        auxiliar.co2_generacion=generacion.cantidadGenerada*tablacons.cons_generacion_panelessolares
    elif generacion.tipo=='Minieolica':
        auxiliar.co2_generacion=generacion.cantidadGenerada*tablacons.cons_generacion_minieolica
#Consumo de vehiculos
    auxiliar.co2_vehiculo=0;
    listaVehiculos = ConsumoVehiculo.objects.filter(nombreTest__nombreTest=nombreTest_id)
    data=0
    if listaVehiculos.count()>0:
        for x in listaVehiculos:
            query = 'https://api.triptocarbon.xyz/v1/footprint?activity=' + str(x.kilometrosSemana) + \
                    '&activityType=miles&country=def&mode=' + x.tipoVehiculo + \
                    '&fuelType=' + x.tipoCombustible

            # Se hace la consulta a la API
            response = urlopen(query)
            res = json.loads(response.read())
            data = data + float(res['carbonFootprint'])

            auxiliar.co2_vehiculo = data
#Consumo de viajes
    auxiliar.co2_viajes=0;
    viajesEmpresa = ViajesEmpresa.objects.filter(nombreTest__nombreTest=nombreTest_id)
    datos=0
    if viajesEmpresa.count()>0:
        for x in viajesEmpresa:
            query = 'https://api.triptocarbon.xyz/v1/footprint?activity=' + str(x.distanciaMedia) + \
                    '&activityType=miles&country=def&mode=' + x.tipoVehiculo + \
                    '&fuelType=' + x.tipoCombustible

            # Se hace la consulta a la API
            response = urlopen(query)
            res = json.loads(response.read())
            datos = datos + float(res['carbonFootprint'])

            auxiliar.co2_viajes = datos


    auxiliar.co2_total=auxiliar.co2_agua+auxiliar.co2_vehiculo+auxiliar.co2_edificios+auxiliar.co2_electricidad+auxiliar.co2_calefaccion+auxiliar.co2_personal+auxiliar.co2_viajes-auxiliar.co2_generacion
    auxiliar.save()
    context={
        'url': nombreTest_id,
        'co2_agua':auxiliar.co2_agua,
        'co2_vehiculo':auxiliar.co2_vehiculo,
        'co2_edificios':auxiliar.co2_edificios,
        'co2_electricidad':auxiliar.co2_electricidad,
        'co2_calefaccion':auxiliar.co2_calefaccion,
        'co2_personal':auxiliar.co2_personal,
        'co2_viajes':auxiliar.co2_viajes,
        'co2_generacion':auxiliar.co2_generacion,
        'co2_total':auxiliar.co2_total,
    }
    return render(request, 'test/resultado.html', context)

def compensacion(request,nombreTest_id):
    auxiliar=TestUsuario.objects.get(nombreTest=nombreTest_id)
    print(auxiliar)
    tablacons=TablaConstantes.objects.get(nombreUsuario=request.user)
    esp=tablacons.cons_compensar_españa*auxiliar.co2_total
    otr=tablacons.cons_compensar_otros*auxiliar.co2_total
    print(auxiliar.co2_total)
    context={
        'url': nombreTest_id,
        'co2_total':auxiliar.co2_total,
        'españa':esp,
        'otros':otr,
    }
    return render(request, 'test/compensacion.html', context)

def vehiculospregunta(request,nombreTest_id):
    context={
        'url': nombreTest_id,
    }
    return render(request, 'test/vehiculospregunta.html', context)

def viajespregunta(request,nombreTest_id):
    context={
        'url': nombreTest_id,
    }
    return render(request, 'test/viajespregunta.html', context)

def home(request):
	 return render(request, 'home.html')

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
            return redirect('../../viajespregunta/'+nombreTest_id)
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

""" 
<---------------------------------------------------------------------------------------------->
<---------------------------------------------------------------------------------------------->
<------------------------------------LOGIN Y REGISTRO------------------------------------------> 
<---------------------------------------------------------------------------------------------->
<---------------------------------------------------------------------------------------------->
"""

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
                #Creamos una tabla de constantes
                constantes = TablaConstantes.objects.create(nombreUsuario=request.user)
                constantes.save()
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


def accederCuenta(request):
    if request.user.is_authenticated:
        alltest = TestUsuario.objects.filter(nombreUsuario=request.user)
        for t in alltest:
            #contamos cuantas instancias de tablas hay asociadas al test, si alguna es 0, lo borramos
            a=ConsumoAgua.objects.filter(nombreTest=t).count()
            ed=ConsumoEdificios.objects.filter(nombreTest=t).count()
            el=ConsumoElectricidad.objects.filter(nombreTest=t).count()
            c=ConsumoCalefaccion.objects.filter(nombreTest=t).count()
            p=PersonalEmpresa.objects.filter(nombreTest=t).count()
            g=GeneracionElectricidad.objects.filter(nombreTest=t).count()
            ve=ConsumoVehiculo.objects.filter(nombreTest=t).count()
            vi=ViajesEmpresa.objects.filter(nombreTest=t).count()
            resultado=a*ed*el*c*p*g*ve*vi
            if resultado == 0:
                """ Esto borra las tablas asociadas
                a=ConsumoAgua.objects.filter(nombreTest=t).delete()
                ed=ConsumoEdificios.objects.filter(nombreTest=t).delete()
                el=ConsumoElectricidad.objects.filter(nombreTest=t).delete()
                c=ConsumoCalefaccion.objects.filter(nombreTest=t).delete()
                p=PersonalEmpresa.objects.filter(nombreTest=t).delete()
                g=GeneracionElectricidad.objects.filter(nombreTest=t).delete()
                ve=ConsumoVehiculo.objects.filter(nombreTest=t).delete()
                vi=ViajesEmpresa.objects.filter(nombreTest=t).delete()"""
                t.delete()

        return redirect('../cuenta/'+request.user.username)
    else:
        return redirect('../login')

def constantesRedirect(request):
    if request.user.is_authenticated:
        tabla = TablaConstantes.objects.get(nombreUsuario=request.user)
        return redirect('../tablaconstantesDetail/' + str(tabla.id))
    else:
        return redirect('../login')

class constantesDetailView(generic.DetailView):
    model = TablaConstantes
    template_name = 'cuenta/tablaconstantes_detail.html'

def constantesModify(request,pk):
    form=TablaConstantesForm()
    if request.method == "POST":
        form = TablaConstantesForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            TablaConstantes.objects.filter(id=pk).update(cons_agua=instancia.cons_agua, 
                cons_edificios_madera=instancia.cons_edificios_madera,cons_edificios_acero=instancia.cons_edificios_acero,cons_edificios_cemento=instancia.cons_edificios_cemento,
                cons_electricidad=instancia.cons_electricidad, 
                cons_calefaccion_gasnatural=instancia.cons_calefaccion_gasnatural,cons_calefaccion_electrico=instancia.cons_calefaccion_electrico,
                cons_calefaccion_carbon=instancia.cons_calefaccion_carbon,cons_calefaccion_gasoleo=instancia.cons_calefaccion_gasoleo,
                cons_personal=instancia.cons_personal, 
                cons_viajes=instancia.cons_viajes,
                cons_generacion_panelessolares=instancia.cons_generacion_panelessolares,cons_generacion_minieolica=instancia.cons_generacion_minieolica,
                cons_compensar_españa=instancia.cons_compensar_españa,cons_compensar_otros=instancia.cons_compensar_otros,)
            return redirect('../../tablaconstantesDetail/'+ pk)
    return render(request, 'cuenta/tablaconstantesmodify.html',{'form': form})