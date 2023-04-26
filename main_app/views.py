from django.shortcuts import render
from .models import Asset


# Create your views here.

def home(request):
    return render(request, 'home.html')

def assets_index(request):
    assets = Asset.objects.all()
    return render(request, 'assets/index.html', {'assets': assets})

def assets_detail(request):
    assets = Asset.objects.all()
    return render(request, 'assets/detail.html', {'assets': assets})

def asset_type(request, asset_type):
    assets = Asset.objects.filter(type=asset_type)
    return render(request, 'assets/list.html', {'assets': assets})