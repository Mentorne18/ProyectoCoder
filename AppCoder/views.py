from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def inicio(request):
    
    return HttpResponse("vista inicio")

def cursos(request):
    
    return HttpResponse("vista cursos")

def profesores(request):
    
    return HttpResponse("Vista profesores")

def estudiantes(request):
    
    return HttpResponse("Vista estudiantes")

def entregables(request):
    
    return HttpResponse("vista entregables")

