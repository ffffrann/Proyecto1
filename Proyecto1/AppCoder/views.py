from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return HttpResponse ("vista inicio")

def cursos(request):
    return render (request, "AppCoder/cursos.html")

def profesores(request):
    return HttpResponse ("vista profesores")

def estudiantes(request):
    return HttpResponse ("vista estudiantes")

def entregables(request):
    return HttpResponse ("vista entregables")