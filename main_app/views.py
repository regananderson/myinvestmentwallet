from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')

def assets_index(request):
    return render(request, 'assets/index.html')