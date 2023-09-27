from django.shortcuts import render
from django.http import HttpResponse


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