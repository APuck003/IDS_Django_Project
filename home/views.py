from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})

def contact(request):
    return render(request, 'home/contact.html', {})

def service(request):
    return render(request, 'home/services.html', {})
