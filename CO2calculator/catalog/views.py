from django.shortcuts import render
from .models import Tabla
from django.views import generic

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .forms import RenewTablaForm

# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_tabla=Tabla.objects.all().count()
    # Libros disponibles (status = 'a')
    #num_instances_available=TablaInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request,'index.html',context={'num_tabla':num_tabla},)

class TablaListView(generic.ListView):
    model = Tabla
    #paginate_by=2 #Pagina automaticamente en grupos de 2, para acceder a la segunda pagina, añadir ?page=2 en la url

class TablaDetailView(generic.DetailView):
    model = Tabla

#@permission_required('catalog.can_mark_returned')
def renew_tabla(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    tabla_inst=get_object_or_404(Tabla, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewTablaForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            tabla_inst.due_back = form.cleaned_data['renewal_date']
            tabla_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewTablaForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/tabla_renew.html', {'form': form, 'tablainst':tabla_inst})

def home(request):
	 return render(request, 'home.html')

def radio_buttons(request):
    return render(request, 'radio.html')

def about(request):
    return render(request, 'about.html')

def calculator(request):
    return render(request, 'calculator.html')

