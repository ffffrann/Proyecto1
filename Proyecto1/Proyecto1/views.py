from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse ("Hola Django equipo coder")

def segunda_vista(request):
    return HttpResponse ("<br><br> <h1>Hola mundo</h1>")


def mi_nombre_es(self, nombre):
    data = f"Mi nombre es: <h1>{nombre}</h1>"
    return HttpResponse (data)

def probando_template(self):
    nombre = "Franco"
    apellido = "Fernandez"

    lista_nombres = ["Franco", "Fidel", "Martina", "Victoria", "Rebecca"]

    diccionario = {
        "nombre" : nombre,
        "apellido" : apellido,
        "lista_nombres": lista_nombres,
    }



    #mi_html = open("C:/Users/54296/Desktop/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #mi_html = loader.get_template("template1.html")
    plantilla = loader.get_template("template1.html")
    #mi_html.close()
    #mi_context = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)