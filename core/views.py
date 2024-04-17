from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/acerca-de/">Acerca de</a></li>
        <li><a href="/portafolio/">Portafolio</a></li>
        <li><a href="/contacto/">Contacto</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + """
                        <h1>Inicio</1>
                        """)

def about(request):
    return HttpResponse(html_base + """
                        <h1>Acerca de</1>
                        """)

def portfolio(request):
    return HttpResponse(html_base + """
                        <h1>Portafolio</1>
                        """)

def contact(request):
    return HttpResponse(html_base + """
                        <h1>Contacto</1>
                        """)
