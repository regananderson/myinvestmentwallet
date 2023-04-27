from django.shortcuts import render
from .models import Asset


# Create your views here.

def home(request):
    assets = Asset.objects.all()
    total_amount = sum(asset.amount for asset in assets)
    total_value = sum(asset.value for asset in assets)
    context = {
        'assets': assets,
        'total_amount': total_amount,
        'total_value': total_value,
    }
    return render(request, 'home.html', context)

# def assets_index(request):
#     assets = Asset.objects.all()
#     return render(request, 'assets/index.html', {'assets': assets})

def assets_index(request):
    assets = Asset.objects.all()
   
    return render(request, 'assets/index.html', {'assets':assets})

def assets_detail(request):
    assets = Asset.objects.all()
    total_amount = sum(asset.amount for asset in assets)
    total_value = sum(asset.value for asset in assets)
    context = {
        'assets': assets,
        'total_amount': total_amount,
        'total_value': total_value,
    }
    return render(request, 'assets/detail.html', context)

def asset_type(request, asset_type):
    assets = Asset.objects.filter(type=asset_type)
    total_amount = sum(asset.amount for asset in assets)
    total_value = sum(asset.value for asset in assets)
    context = {
        'assets': assets,
        'total_amount': total_amount,
        'total_value': total_value,
    }
    return render(request, 'assets/list.html', context)

def investments_detail(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    return render(request, 'investments/detail.html', {'asset':asset})
