
from django.urls import path

from AppCoder import views

urlpatterns = [
    
    path("", views.inicio), #Esta es nuestra 1er view
    path("cursos", views.cursos, name="Cursos"),
    path("profesores", views.profesores, name="Profesores"),
    path("estudiantes", views.estudiantes, name="Estudiantes"),
    path("entregables", views.entregables, name="Entregables"),
    
]