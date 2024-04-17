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
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/home.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")
