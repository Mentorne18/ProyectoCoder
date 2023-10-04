from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso #para traer Curso de models y usarlo en la validación de datos enviados.
from AppCoder.forms import CursoFormulario

# Create your views here.


# def inicio(request):
    
#     return HttpResponse("vista inicio")

# def cursos(request):
    
#     return HttpResponse("vista cursos")

# def profesores(request):
    
#     return HttpResponse("Vista profesores")

# def estudiantes(request):
    
#     return HttpResponse("Vista estudiantes")

# def entregables(request):
    
#     return HttpResponse("vista entregables")    ESTO YA NO VA PORQUE LO REEMPLAZAMOS POR EL RENDER DE LA PLANTILLA

def inicio(request):
    
    return render(request, "appCoder/index.html")

def cursos(request):
    
    return render(request, "appCoder/cursos.html")

def profesores(request):
    
    return render(request, "appCoder/profesores.html")

def estudiantes(request):
    
    return render(request, "appCoder/estudiantes.html")

def entregables(request):

    return render(request, "appCoder/entregables.html")

def cursoFormulario(request):
    
    if request.method == "POST":
        
        miFormulario = CursoFormulario(request.POST) # aca nos llega toda la info del html
        
        print(miFormulario)
        
        if miFormulario.is_valid(): #if para ver si pasa la validación de django
            
            informacion = miFormulario.cleaned_data
            
            curso = Curso (nombre=informacion["curso"], camada=informacion["camada"])
            
            curso.save()
            
            return render(request, "AppCoder/inicio.html") #aca volvemos al inicio de la pagina luego del registro o podemos elegir donde querramos.
        
    else:
        
        miFormulario = CursoFormulario() #Formulario vacio para construir el html. Al llamarla con los campos vacios, devuelve este valor.
        
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

