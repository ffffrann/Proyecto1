from django.urls import path
from AppCoder.views import * #inicio, cursos, entregables, estudiantes, profesores, setEstudiantes, getEstudiantes, buscarEstudiante

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path("cursos/", cursos, name="Cursos"),
    path("entregables/", entregables, name="Entregables"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("profesores/", profesores, name="Profesores"),
    path("setEstudiantes/", setEstudiantes, name="setEstudiantes"),
    path("getEstudiantes/", getEstudiantes, name="getEstudiantes"),
    path("buscarEstudiantes/", buscarEstudiante, name="buscarEstudiantes"),

]