from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# Create your views here.

def index(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiantes = Estudiante.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': len(estudiantes)}
    return render(request, 'index.html', informacion_template)


def obtener_estudiante(request, id):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiante = Estudiante.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiante': estudiante}
    return render(request, 'obtener_estudiante.html', informacion_template)


def crear_estudiante(request):
    """
    """
    print(request)
    if request.method=='POST':
        formulario = EstudianteForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEstudiante.html', diccionario)


def editar_estudiante(request, id):
    """
    """
    print("---------------")
    print(request)
    print("---------------")
    estudiante = Estudiante.objects.get(pk=id)
    # Deber: consultar
    if request.method=='POST':
        formulario = EstudianteForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm(instance=estudiante)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEstudiante.html', diccionario)


def eliminar_estudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    estudiante.delete()
    return redirect(index)


def listar_paises(request):
    # Obtenemos todos los objetos Pais de la base de datos usando el ORM de Django.
    paises = Pais.objects.all()
    
    # Preparamos la información que se enviará a la plantilla HTML.
    # Incluimos la lista de países y el número total de países.
    informacion_template = {
        'paises': paises,
        'numero_paises': len(paises)
    }
    
    return render(request, 'index_pais.html', informacion_template)

def agregar_pais(request):
    # Si la solicitud es de tipo POST (es decir, el formulario fue enviado)
    if request.method == 'POST':
        # Creamos una instancia del formulario con los datos enviados por el usuario.
        formulario = PaisForm(request.POST)
        
        # Verificamos si los datos del formulario son válidos.
        if formulario.is_valid():
            # Si son válidos, guardamos el nuevo objeto Pais en la base de datos.
            formulario.save()
            
            return redirect('index_pais')
    else:
        formulario = PaisForm()
    
    # Preparamos un diccionario con el formulario para pasarlo a la plantilla HTML.
    diccionario = {'formulario': formulario}
    
    return render(request, 'agregar_pais.html', diccionario)