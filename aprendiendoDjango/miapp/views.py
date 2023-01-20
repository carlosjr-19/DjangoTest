from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#MVC = Modelo Vista Controlador  -> Acciones (metodos)
#MVT = Modelo Template Vista -> Acciones (metodos)

layaut = """

<h1> Sitio web con Django</h1>
<hr>
<ul>
    <li><a href="/inicio">Inicio</a>
    <li><a href="/hola-mundo">Hola mundo</a>
    <li><a href="/pagina-pruebas">Pagina</a>
    <li><a href="/contacto">Contactos</a>
</ul>
<hr>
"""


def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
        """

    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return render(request, 'index.html')

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):
    if redirigir == 12:
        return redirect('/inicio/')

    return render(request, 'pagina.html')

def contacto(request, nombre=""):
    return HttpResponse(layaut + f"<h2>Contacto {nombre}</h2>")

