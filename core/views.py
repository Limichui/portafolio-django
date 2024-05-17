from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def resume(request):
    return render(request, "core/resume.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def services(request):
    return render(request, "core/services.html")

def contact(request):
    return render(request, "core/contact.html")
